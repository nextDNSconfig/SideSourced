import logging

from altparse import AltSourceManager, Parser, altsource_from_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

########################
## WUXU-COMPLETE
########################

sourcesData = [
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://ipa.cypwn.xyz/cypwn.json"},
        "ids": ["it.ned.appdb-ios"],
        "ignoreNews": True
    },
    {
        "parser": Parser.UNC0VER,
        "kwargs": {"url": "https://unc0ver.dev/releases.json"},
        "ids": ["science.xnu.undecimus"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://taurine.app/altstore/taurinestore.json"},
        "ids": ["org.coolstar.taurine"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://theodyssey.dev/altstore/odysseysource.json"},
        "ids": ["org.coolstar.odyssey"]
    }
]
alternateAppData = {

    "it.ned.appdb-ios": {
        "name" : "AppDB Client",
        "developerName" : "ned",
        "subtitle" : "A fully-featured iOS client for appdb.to",
        "localizedDescription" : "AppDB Client is a fully featured app aiming to provide a better experience for every appdb user\n\nFeatures:\n\n• Easily browse appdb database with a blazing fast and smooth user interface\n• Control all your appdb linked devices\n• Install any content to your device after authorizing the app\n• Dowload IPAs from the web and install them right away\n• MyAppStore & Automatic Requests integration!\n• A wonderful dark mode\n• iOS 14 homescreen Widgets!\n\nAnd a lot more…",
        "iconURL" : "https://static.appdb.to/images/cydia-1900000538-icon.png",
        "tintColor" : "#0365a0",
        "screenshotURLs" : [
            "https://static.appdb.to/images/cydia-1900000538-iphone-0-1615476553.png",
            "https://static.appdb.to/images/cydia-1900000538-iphone-1-1615476554.png",
            "https://static.appdb.to/images/cydia-1900000538-iphone-2-1615476554.png",
            "https://static.appdb.to/images/cydia-1900000538-iphone-3-1615476555.png"
        ]
    },
    "science.xnu.undecimus": {
        "name" : "unc0ver",
        "developerName" : "Pwn20wnd",
        "subtitle" : "The most advanced jailbreak tool.",
        "localizedDescription" : "unc0ver is an advanced jailbreaking tool for iOS devices. Jailbreaking with unc0ver unlocks the true power of your iDevice. Customize the appearance of your device, gain full control over how your device operates, obtain access to hidden features of iOS, and more.\n\nCompatibility:\n• unc0ver supports iOS 11.0 through to iOS 14.3 (Excluding 13.5.1 and 13.3.1)\n\nStability:\n• Utilizing the latest stable APT and Mobile Substrate, stability is guaranteed.\n\nSecurity:\n• Utilizing native system sandbox exceptions, security remains intact while enabling access to jailbreak files.",
        "iconURL" : "https://i.imgur.com/5aehDxj.png",
        "tintColor" : "#515151",
        "screenshotURLs" : [
            "https://i.imgur.com/ItMaRRV.png",
            "https://i.imgur.com/bjzyqpY.png",
            "https://i.imgur.com/3TMGkaO.png",
            "https://i.imgur.com/gTYfncm.png"
        ]
    },
    "org.coolstar.taurine": {
        "name" : "Taurine",
        "developerName" : "Odyssey Team",
        "subtitle" : "Time to get amped.",
        "localizedDescription" : "Taurine is an iOS 14.0-14.3 jailbreak, utilizing Procursus and Libhooker.",
        "iconURL" : "https://taurine.app/assets/images/icon.png",
        "tintColor" : "#9e3a47",
        "screenshotURLs" : [
            "https://taurine.app/assets/images/ss-1.png",
            "https://taurine.app/assets/images/ss-2.png",
            "https://taurine.app/assets/images/ss-3.png"
        ]
    },
    "org.coolstar.odyssey": {
        "name" : "Odyssey",
        "developerName" : "Odyssey Team",
        "subtitle" : "A new jailbreak for a new era.",
        "localizedDescription" : "Supporting iOS Versions: 13.0 - 13.7.\n\nOdyssey is the first jailbreak to be written almost entirely in Swift. Completely open source and welcomes community contributions and pull requests, as a tribute to the dearly departed s0uthwes and his continued optimism and faith in the project. Comes with the open source Procursus bootstrap, designed from the ground up with openness and compatiblity in mind. Along with a new tweak injection platform, libhooker.",
        "iconURL" : "https://theodyssey.dev/assets/images/icon.png",
        "tintColor" : "#9766a7",
        "screenshotURLs" : [
            "https://theodyssey.dev/assets/images/ss-1.png",
            "https://theodyssey.dev/assets/images/ss-2.png",
            "https://theodyssey.dev/assets/images/ss-3.png"
        ]
    }
}

src = altsource_from_file("wuxu-complete.json")
wuxuslib = AltSourceManager(src, sourcesData)
try:
    wuxuslib.update()
    wuxuslib.alter_app_info(alternateAppData)
    wuxuslib.save()
    wuxuslib.save(alternate_dir="dist/wuxu-complete.min.json",prettify=False)
except Exception as err:
    logging.error(f"Unable to update {wuxuslib.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")

########################
## WUXU-COMPLETE++
########################

sourcesData = [
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://ipa.cypwn.xyz/cypwn.json"},
        "ids": ["com.microblink.PhotoMath", "com.hammerandchisel.discord"],
        "ignoreNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://qnblackcat.github.io/AltStore/apps.json"},
        "ids": ["com.google.ios.youtube","com.facebook.Facebook"],
        "ignoreNews": True
    }
]

alternateAppData = {
    
    "com.microblink.PhotoMath": {
        "name" : "Photomath++",
        "developerName" : "Strejda603",
        "subtitle" : "Photomath with plus activated!",
        "localizedDescription" : "Photomath works as normal, only the premium features are activated as if you bought them.",
        "iconURL" : "https://img.ipa4fun.com/c9/1d/c3/919087726-logo.jpg",
        "tintColor" : "#830824",
        "screenshotURLs" : [
            "https://img.ipa4fun.com/c9/1d/c3/919087726-screenshot-1.jpg",
            "https://img.ipa4fun.com/c9/1d/c3/919087726-screenshot-2.jpg",
            "https://img.ipa4fun.com/c9/1d/c3/919087726-screenshot-3.jpg",
            "https://img.ipa4fun.com/c9/1d/c3/919087726-screenshot-4.jpg",
            "https://img.ipa4fun.com/c9/1d/c3/919087726-screenshot-5.jpg"
        ]
    },
    "com.hammerandchisel.discord": {
        "name" : "Discord++",
        "developerName" : "Enmity Team",
        "subtitle" : "The power of addons, all in your hand.",
        "localizedDescription" : "Add plugins and themes to Discord!\n\n\nTo get plugins & themes go to the official Enmity discord\n\nhttps://discord.gg/enmity",
        "iconURL" : "https://img.ipa4fun.com/87/01/a2/985746746-logo.jpg",
        "tintColor" : "#3c45ac",
        "screenshotURLs" : [
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-1.jpg",
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-2.jpg",
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-3.jpg",
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-4.jpg",
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-5.jpg",
            "https://img.ipa4fun.com/87/01/a2/985746746-screenshot-6.jpg"
        ]
    },
    "com.google.ios.youtube": {
        "name" : "YouTube++",
        "developerName" : "qnblackcat",
        "subtitle" : "All-In-One Tweak for YouTube.",
        "localizedDescription" : "If you’re a YouTube app user then you’ll have to take advantage of uYou tweak.\n\nWith uYou, you can enjoy video and audio downloads with importing features, play videos in PiP (Picture In Picture), background audio playback, and a whole lot of other features that are usually restricted/not available in the YouTube app.\n\nuYou will add an icon button on the top right corner (beside the search icon) to show the Downloads/Downloading list.\nYou can also access uYou's settings from the Downloads list.\n\nFeatures:\n\n• Remove YouTube Ads.\n• Background playback for YT videos.\n• Download Videos/Audio/Shorts for offline playback (supports up to 4K).\n• Support all YT Formats (MP4 + WebM), all qualities (from 144p to 4K) and all frames (30fps, 50fps, and 60fps).\n• Play saved media in a custom player with background playback support.\n• Supports mini-player for easier navigation.\n• Supports scrubbing/controls from Control Center.\n• Share/Export saved videos to Camera Roll or to any other app.\n• Gestures Controls on Video (Swipe Left/Right to increase/decrease Volume/Brightness/Seek).\n• Playback Speed Controls.\n• Play videos in PiP (Picture In Picture).\n• iPad layout style.\n• Sideloaded iPA.\n• In-app Settings.\n• Support Cercube and DLEasy migration to move all of your downloads into uYou with a tap of a button.\n• More options are in the settings.",
        "iconURL" : "https://img.ipa4fun.com/65/82/9f/544007664-logo.jpg",
        "tintColor" : "#af0303",
        "screenshotURLs" : [
            "https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/25/84/db/2584db5e-1b7d-197f-1a33-13602daf5d95/f1192f1f-430d-469a-b032-cdf77b8b04c7_iOS-5.5-in_1.jpg/2048x0w.jpg",
            "https://is1-ssl.mzstatic.com/image/thumb/Purple126/v4/54/0a/8d/540a8daf-4cc2-397a-e1b1-90b859947b44/868afd15-b2e4-4923-b0f8-c5599327a3d7_iOS-5.5-in_2.jpg/2048x0w.jpg",
            "https://is3-ssl.mzstatic.com/image/thumb/Purple126/v4/a1/e3/e8/a1e3e81c-94e1-9bc2-c5f6-f5efe2814230/2930dbc3-4228-403b-b46d-e0066516ab6a_iOS-5.5-in_3.jpg/2048x0w.jpg",
            "https://is2-ssl.mzstatic.com/image/thumb/Purple126/v4/9e/cd/9b/9ecd9b66-ade4-70f8-a6f6-7b1ee3cc7b41/45519fca-0e0b-466e-9ed6-9a43232a0bf8_iOS-5.5-in_4.jpg/2048x0w.jpg",
            "https://is5-ssl.mzstatic.com/image/thumb/Purple126/v4/90/e2/4b/90e24bd5-b81b-558a-3b1a-e5acf46a7669/bace9abd-71f3-4700-8adf-cedcba275a67_iOS-5.5-in_5.jpg/2048x0w.jpg"
        ]
    },
        "com.facebook.Facebook": {
        "name" : "Facebook++",
        "developerName" : "Michael Lema",
        "subtitle" : "Facebook with a number of new features!",
        "localizedDescription" : "Facebook Wolf brings a number of new features to Facebook such as:\n\nUser\n• Disable marking messages as seen\n• Disable typing status in messages\n• No feed ads\n\nStory\n• Disable marking stories\n• Disable auto-advance in stories\n• Save Story images and videos\n• No story ads\n\nFeed\n• Save Feed videos by long-pressing the video\n\nAnd more!",
        "iconURL" : "https://img.ipa4fun.com/92/c2/a0/284882215-logo.jpg",
        "tintColor" : "#034ea0",
        "screenshotURLs" : [
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-1.jpg",
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-2.jpg",
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-3.jpg",
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-4.jpg",
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-5.jpg",
            "https://img.ipa4fun.com/92/c2/a0/284882215-screenshot-6.jpg"
        ]
    }
}

src = altsource_from_file("wuxu-complete++.json")
wuxuslib_plus = AltSourceManager(src, sourcesData)
try:
    wuxuslib_plus.update()
    wuxuslib_plus.alter_app_info(alternateAppData)
    wuxuslib_plus.save()
    wuxuslib_plus.save(alternate_dir="dist/wuxu-complete++.min.json",prettify=False)
except Exception as err:
    logging.error(f"Unable to update {wuxuslib_plus.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
