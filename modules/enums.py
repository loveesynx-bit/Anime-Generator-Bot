from enum import Enum

class PicType(Enum):
    SFW = "sfw"
    NSFW = "nsfw"

class PicCategory(Enum):
    """
    It can be used as `if PicType.TYPE.value in PicCategory.CATEGORY.allowed_types`
    Enum values map directly to waifu.im tag slugs.
    """
    WAIFU = "waifu"
    MAID = "maid"
    SELFIES = "selfies"
    UNIFORM = "uniform"
    MARIN = "marin-kitagawa"
    MORI = "mori-calliope"
    OPPAI = "oppai"
    ECCHI = "ecchi"
    HENTAI = "hentai"
    MILF = "milf"
    ASS = "ass"
    ORAL = "oral"
    PAIZURI = "paizuri"
    ERO = "ero"

    @property
    def allowed_types(self):
        allowed = {
            PicCategory.WAIFU: {"sfw", "nsfw"},
            PicCategory.MAID: {"sfw"},
            PicCategory.SELFIES: {"sfw"},
            PicCategory.UNIFORM: {"sfw", "nsfw"},
            PicCategory.MARIN: {"sfw"},
            PicCategory.MORI: {"sfw"},
            PicCategory.OPPAI: {"nsfw"},
            PicCategory.ECCHI: {"nsfw"},
            PicCategory.HENTAI: {"nsfw"},
            PicCategory.MILF: {"nsfw"},
            PicCategory.ASS: {"nsfw"},
            PicCategory.ORAL: {"nsfw"},
            PicCategory.PAIZURI: {"nsfw"},
            PicCategory.ERO: {"nsfw"},
        }
        return allowed[self]
