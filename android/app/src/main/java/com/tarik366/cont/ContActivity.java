package com.tarik366.cont;

import org.libsdl.app.SDLActivity;

public class ContActivity extends SDLActivity {
	@Override
	protected String[] getLibraries() {
		return new String[] {
			"SDL3",
			"SDL3_image",
			// "SDL3_mixer",
			// "SDL3_net",
			"SDL3_ttf",
			"xml2",
			"cont"
		};
	}
}