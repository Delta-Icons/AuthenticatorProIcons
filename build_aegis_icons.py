#!/usr/bin/env python3

from util.basic_builder import BasicBuildSettings, build_basic_pack


def main():
    settings = BasicBuildSettings()
    settings.repo_url = "https://github.com/Delta-Icons/aegis-icons.git"
    settings.svg_glob = ["icons", "**", "*.svg"]
    settings.output_name = "aegis-icons"
    settings.pack_name = "Aegis Icons"
    settings.pack_description = "delta version of the unofficial monochrome-styled 2FA icons for open source Android authenticator Aegis"
    settings.pack_url = "https://github.com/Delta-Icons/aegis-icons"

    build_basic_pack(settings)


if __name__ == "__main__":
    main()
