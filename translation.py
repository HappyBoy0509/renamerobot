class Translation(object):
    START_TEXT = """Hello,
This is Rename Robot!

<b>Please Send Me Any Telegram file And \n Reply to that file to /rename New Name.NameExtension(eg.mp4,mkv,avi,zip,apk,rar...)</b>

/help For More Details.."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = " /help for Details"
    DOWNLOAD_START = "trying to download"
    UPLOAD_START = "trying to upload"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me🤓 \nSupport HB4All @HB4All.**"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Support HB4All @HB4All_Bot"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}..\nIf you think this is a bug, please contact <a href='https://t.me./hb4all1_bot'>@HB4All</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail Saved. This Image Will Be Used In The File."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hi I am Rename Robot..
    
1. Send me any Telegram File.
2. Reply to that message to /rename new name.extension
   
Support HB4All @HB4All_bot"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.."
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Only 1 Request Per 30 minutes.
or Try 1800 seconds later."""
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.
<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""
