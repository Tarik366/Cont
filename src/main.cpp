#include <ui.h>
#include <connection.h>
#include <iostream>
#include <thread>

int main() {
    std::thread ui_thread(uiHandler);
    sendPacket();
    ui_thread.join();

    return 1;
}