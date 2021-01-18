# Copyright (C) 2020-2021 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# For NaytSeyd ️️❤️ Saniye
#


from time import sleep
from random import choice
from sedenecem.core import edit, sedenify
# ================= CONSTANT =================
SANIYE_STRINGS = [
    "blyrm🥺", "hallo", "nbr ex svglm", "evt🥺", "tamam askm", "hosgeldin askm",
    "handicap", "jeg elsker dig", "ja", "ben uyuyorum, ig bebeler", "tmm cool",
    "cool bruh", "bn varim🥺", "kstm", "@NightShade slk amd", "sefsz amd",
    "amd skm", "ezk amd", "eeee😒", "bu ne lan Vsjjsbsjs", "uuuuu",
    "gelin kuzucuklrm", "amedi skm", "ex svglilrm",
    "svglm olmak istyenlr dm gelsn", "ikinizden ayriliyrm", "ayb krcm🥺",
    "ve ii gclr bkr ❤️", "sn kmsn", "ekle bnie", "pika pikaaaaaaa",
    "gule gule kullan", "cnku tg skm", "banane smk", "bkr skm",
    "slk bkre dedim", "slm gzlm", "iimsn", "kayiplarda",
    "snie gørdm dha ii oldm", "hello askm", "slk baris", "karima sg deme",
    "sen haketmistin..", "kiyamam ki", "bana sg demen... 🥺", "hyr yalan",
    "sen uzuyon", "beni cok uzuyorsun", "ecm skm",
    "tmm küs, gece dc glmcm ozmn", "iyi gecelr 🌸", "yengenim", "eed askm",
    "yemek yiyip gelcm bebislerm", "sapikmisin", "bana tapacaksin burda",
    "nzbdbshajahahhq yazik", "komik olan ne", "belki gørdum nrdn biliyn",
    "pjmani skm", "gle beraber uyuyalm", "ama uykm var🥺", "tm cok coolsn",
    "bi susarmisiniz", "oglum sikrirtme kendini", "ingilizceni skm",
    "buna gulecekmiydim", "søv ona", "@NightShade bana yavsiyo bu🥺",
    "saniyeman ol", "eed puskuvut", "kutlay benim askim, ona yuruyemezsin😠",
    "@NightShade amd😠", "bnie hep uzuyo🥺", "shhshshsha",
    "bn derim senin yerine", "kanka deme lazim olr",
    "seni gece ariyacam, kacta musaitsin", "ppn cko hos. svglm olrmsn",
    "amd aglsn", "hiiiiio, happy bday ona ozaman",
    "bildigim kadariyla u were tek kid", "jesus christ",
    "o neydi lan zbnsshjaka", "tamam ozaman afettim🥺",
    "alisdim artik beni uzmene...", "resimlerini siliyom...",
    "seni cko øzledim❤️", "@NightShade 💞",
    "bana dc girin diyorsunuz, beni takmiyorsunuz srfszlr", "kalbime gir",
    "hadi see u", "bu gece de ben konusamam 🥺",
    "bn cikiom tgden birazdan, instageamdan yazarsn",
    "sn iyi degilken bende iyi olamam 🥺", "nazar degdi :(", "snie øzldm",
    "bende sana atmistim, sende stickers yaptin :(", "yeterince cool degilsn",
    "wowoowowowow", "uwuwuwuwuwu", "elni at"]
# ================= CONSTANT =================


@sedenify(pattern='^.saniye')
def saniyeify(message):
    saniye(message)


def saniye(message):
    edit(message, choice(SANIYE_STRINGS))


@sedenify(pattern='^.saniş$')
def sanis(message):
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    edit(
        message,
        '[Saniş](tg://user?id=623847224) 💘 [NaytSeyd](tg://user?id=551728027)')
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️❤️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n❤️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n❤️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️❤️\n◼️◼️◼️◼️◼️`",
        "`◼️❤️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️❤️◼️`",
        "`◼️◼️◼️❤️◼️\n◼️◼️◼️◼️◼️\n◼️🧛🏻‍♂️❤️🧛🏻‍♀️◼️\n◼️◼️◼️◼️◼️\n◼️❤️◼️◼️◼️`",
    ]
    for i in animation_ttl:
        sleep(animation_interval)
        edit(message, animation_chars[i % len(animation_chars)])


@sedenify(pattern='^.snş$')
def sns(message):
    animation_interval = 0.5
    animation_ttl = range(0, 7)
    edit(message, "Saniş ❤️")
    animation_chars = [
        "S_",
        "SA_",
        "SAN_",
        "SANİ_",
        "SANİŞ_",
        "SANİŞ❤_",
        "[Saniş](tg://user?id=623847224) 💘 [NaytSeyd](tg://user?id=551728027)",
    ]
    for i in animation_ttl:
        sleep(animation_interval)
        edit(message, animation_chars[i % len(animation_chars)])


@sedenify(pattern='^.naytsaniş$')
def naytsanis(message):
    animation_interval = 1
    animation_ttl = range(0, 6)
    edit(
        message,
        '[Saniş](tg://user?id=623847224) 💘 [NaytSeyd](tg://user?id=551728027)')
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ NaytSeyd   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀❤️⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Saniş   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀❤️⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ NaytSeyd   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀❤️⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Saniş  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀❤️ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ NaytSeyd   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀❤️ ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Saniş   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀❤️⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃ ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`", ]
    for i in animation_ttl:
        sleep(animation_interval)
        edit(message, animation_chars[i % len(animation_chars)])


@sedenify(pattern='^.❤️$')
def sanisveamed(message):
    edit(
        message, "⠀⠀`.-----.    .-----.    `\n"
        r"` /       '..'       \   `\n"
        "`|                    |  `\n"
        "`|       Ahmet        |  `\n"
        r"` \      Saniş       /   `\n"
        r"`  \                /    `\n"
        r"`   '\            /'     `\n"
        r"`     '\        /'       `\n"
        r"`       '\    /'         `\n"
        r"`         '\/'           `\n"
        "            [Saniş](tg://user?id=623847224) 💘 [NaytSeyd](tg://user?id=551728027)")
