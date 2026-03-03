

#include <iostream>
#include <stdexcept>

#include <config.h>

#include <hv/UdpClient.h>
#include <hv/htime.h>

using namespace hv;

void sendPacket() {
    Config config;
    const char* remote_host = config.conf_table["connection"]["host"].as<std::string>().c_str(); 
    int remote_port = config.conf_table["connection"]["port"].as<int>();

    printf("%s:%i", remote_host, remote_port);

    UdpClient cli;
    int sockfd = cli.createsocket(remote_port, remote_host);
    if (sockfd < 0) {
        return throw std::runtime_error(std::format("Socket cannot created"));
    }
    printf("client sendto port %d, sockfd=%d ...\n", remote_port, sockfd);
    cli.onMessage = [](const SocketChannelPtr& channel, Buffer* buf) {
        printf("< %.*s\n", (int)buf->size(), (char*)buf->data());
    };
    cli.start();

    // sendto(time) every 3s
    cli.loop()->setInterval(3000, [&cli](TimerID timerID) {
        char str[DATETIME_FMT_BUFLEN] = {0};
        datetime_t dt = datetime_now();
        datetime_fmt(&dt, str);
        cli.sendto(str);
    });

    std::string str;
    while (std::getline(std::cin, str)) {
        if (str == "close") {
            cli.closesocket();
        } else if (str == "start") {
            cli.start();
        } else if (str == "stop") {
            cli.stop();
            break;
        } else {
            cli.sendto(str);
        }
    }

}