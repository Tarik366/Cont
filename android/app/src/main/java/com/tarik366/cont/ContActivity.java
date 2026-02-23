package com.tarik366.cont;

import org.libsdl.app.SDLActivity;

public class ContActivity extends SDLActivity {
	@Override
	protected String[] getLibraries() {
		return new String[] {
			"SDL2",
			"SDL2_image",
			// "SDL2_mixer",
			// "SDL2_net",
			"SDL2_ttf",
			"xml2",
			"vanilla"
		};
	}
}