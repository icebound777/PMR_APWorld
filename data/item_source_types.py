# see ItemHints.patch in StarRod mod files
SRC_NONE = 0
SRC_LAYINGAROUND = 1
SRC_CHEST = 2
SRC_CRATE = 3
SRC_ITEMBLOCK = 4
SRC_HIDDENBLOCK = 5
SRC_HIDDENTILE = 6
SRC_GIVENBYNPC = 7
SRC_SOLDBYNPC = 8
SRC_DROPPEDBYENEMY = 9
SRC_HIDDENINTREE = 10
SRC_HIDDENINBUSH = 11
SRC_HIDDENINVINES = 12
SRC_UNDERWATER = 13
SRC_GROUNDPOUND = 14

item_source_types = {
    # Goomba Region
    "KMR_00": {"HiddenPanel": SRC_HIDDENTILE,},
    "KMR_02": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "GiftE": SRC_GIVENBYNPC,
               "GiftF": SRC_GIVENBYNPC,
               "ItemA": SRC_LAYINGAROUND,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Partner": SRC_GIVENBYNPC,
               "Bush2_Drop1": SRC_HIDDENINBUSH},
    "KMR_03": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "YBlockA": SRC_ITEMBLOCK,
               "HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "KMR_04": {"Tree3_Drop1A": SRC_HIDDENINTREE,
               "Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush2_Drop1": SRC_HIDDENINBUSH,
               "Bush3_Drop1A": SRC_HIDDENINBUSH,
               "Bush3_Drop1B": SRC_HIDDENINBUSH,
               "Bush4_Drop1": SRC_HIDDENINBUSH,
               "Bush5_Drop1": SRC_HIDDENINBUSH,
               "Tree1_Drop1": SRC_HIDDENINTREE,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "Bush7_Drop1": SRC_HIDDENINBUSH,
               "RandomBlockItemA": SRC_ITEMBLOCK},
    "KMR_05": {"ItemA": SRC_LAYINGAROUND,
               "Tree1_Drop1A": SRC_HIDDENINTREE},
    "KMR_06": {"ItemA": SRC_LAYINGAROUND,
               "RBlockA": SRC_ITEMBLOCK,},
    "KMR_09": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},
    "KMR_10": {"ChestA": SRC_CHEST,
               "YBlockA": SRC_ITEMBLOCK,},
    "KMR_11": {"HiddenPanel": SRC_HIDDENTILE,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "YBlockA": SRC_HIDDENBLOCK,},
    "KMR_20": {"GiftA": SRC_GIVENBYNPC,},

# Toad Town
    "MAC_00": {"ItemA": SRC_LAYINGAROUND,
               "GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,
               "DojoA": SRC_GIVENBYNPC,
               "DojoB": SRC_GIVENBYNPC,
               "DojoC": SRC_GIVENBYNPC,
               "DojoD": SRC_GIVENBYNPC,
               "DojoE": SRC_GIVENBYNPC},
    "MAC_01": {"ItemA": SRC_GROUNDPOUND,
               "GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "ShopBadgeA": SRC_SOLDBYNPC,
               "ShopBadgeB": SRC_SOLDBYNPC,
               "ShopBadgeC": SRC_SOLDBYNPC,
               "ShopBadgeD": SRC_SOLDBYNPC,
               "ShopBadgeE": SRC_SOLDBYNPC,
               "ShopBadgeF": SRC_SOLDBYNPC,
               "ShopBadgeG": SRC_SOLDBYNPC,
               "ShopBadgeH": SRC_SOLDBYNPC,
               "ShopBadgeI": SRC_SOLDBYNPC,
               "ShopBadgeJ": SRC_SOLDBYNPC,
               "ShopBadgeK": SRC_SOLDBYNPC,
               "ShopBadgeL": SRC_SOLDBYNPC,
               "ShopBadgeM": SRC_SOLDBYNPC,
               "ShopBadgeN": SRC_SOLDBYNPC,
               "ShopBadgeO": SRC_SOLDBYNPC,
               "ShopBadgeP": SRC_SOLDBYNPC,},
    "MAC_02": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "ItemA": SRC_LAYINGAROUND,
               "HiddenPanel": SRC_HIDDENTILE,},
    "MAC_03": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,},
    "MAC_04": {"ItemA": SRC_GIVENBYNPC,
               "ItemB": SRC_GIVENBYNPC,
               "ItemC": SRC_GIVENBYNPC,
               "ItemD": SRC_GIVENBYNPC,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "MAC_05": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},

# Toad Town Tunnels
    "TIK_02": {"ChestA": SRC_CHEST},
    "TIK_03": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,},
    "TIK_05": {"ChestA": SRC_CHEST},
    "TIK_07": {"ItemA": SRC_LAYINGAROUND,
               "RandomBlockItemA": SRC_ITEMBLOCK},
    "TIK_10": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "HiddenYBlockC": SRC_HIDDENBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "TIK_12": {"RandomBlockItemA": SRC_ITEMBLOCK},
    "TIK_15": {"GiftA": SRC_SOLDBYNPC,
               "GiftB": SRC_SOLDBYNPC,
               "GiftC": SRC_SOLDBYNPC,
               "GiftD": SRC_SOLDBYNPC,
               "GiftE": SRC_SOLDBYNPC,
               "GiftF": SRC_SOLDBYNPC,
               "GiftG": SRC_SOLDBYNPC,
               "GiftH": SRC_SOLDBYNPC,
               "GiftI": SRC_SOLDBYNPC,
               "GiftJ": SRC_SOLDBYNPC,
               "GiftK": SRC_SOLDBYNPC,},
    "TIK_17": {"RandomBlockItemA": SRC_ITEMBLOCK},
    "TIK_18": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "TIK_19": {"RandomBlockItemA": SRC_ITEMBLOCK},
    "TIK_20": {"YBlockA": SRC_ITEMBLOCK},
    "TIK_21": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,
               "YBlockD": SRC_ITEMBLOCK,
               "YBlockE": SRC_ITEMBLOCK,},
    "TIK_23": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "HiddenYBlockC": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,},
    "TIK_24": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},
    "TIK_25": {"BigChest": SRC_CHEST,},

# Peach's Castle
    "KKJ_16": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,},
    "KKJ_17": {"ItemA": SRC_LAYINGAROUND},
    "KKJ_20": {"ChestA": SRC_CHEST},

# Shooting Star Summit
    "HOS_00": {"HiddenPanel": SRC_HIDDENTILE,},
    "HOS_01": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_LAYINGAROUND,},
    "HOS_03": {"ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "HOS_06": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "ShopBadgeA": SRC_SOLDBYNPC,
               "ShopBadgeB": SRC_SOLDBYNPC,
               "ShopBadgeC": SRC_SOLDBYNPC,
               "ShopBadgeD": SRC_SOLDBYNPC,
               "ShopBadgeE": SRC_SOLDBYNPC,
               "ShopBadgeF": SRC_SOLDBYNPC,
               "ShopBadgeG": SRC_SOLDBYNPC,
               "ShopBadgeH": SRC_SOLDBYNPC,
               "ShopBadgeI": SRC_SOLDBYNPC,
               "ShopBadgeJ": SRC_SOLDBYNPC,
               "ShopBadgeK": SRC_SOLDBYNPC,
               "ShopBadgeL": SRC_SOLDBYNPC,
               "ShopBadgeM": SRC_SOLDBYNPC,
               "ShopBadgeN": SRC_SOLDBYNPC,
               "ShopBadgeO": SRC_SOLDBYNPC,
               "ShopRewardA": SRC_GIVENBYNPC,
               "ShopRewardB": SRC_GIVENBYNPC,
               "ShopRewardC": SRC_GIVENBYNPC,
               "ShopRewardD": SRC_GIVENBYNPC,
               "ShopRewardE": SRC_GIVENBYNPC,
               "ShopRewardF": SRC_GIVENBYNPC,},

# Koopa Region
    "NOK_01": {"Bush1_Drop1A": SRC_HIDDENINBUSH,
               "Bush3_Drop1A": SRC_HIDDENINBUSH,
               "Bush4_Drop1A": SRC_HIDDENINBUSH,
               "Bush5_Drop1A": SRC_HIDDENINBUSH,
               "Bush6A_Drop1A": SRC_HIDDENINBUSH,
               "Bush7A_Drop1A": SRC_HIDDENINBUSH,
               "GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "NOK_02": {"Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush6_Drop1": SRC_HIDDENINBUSH,
               "GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "GiftD": SRC_GIVENBYNPC,
               "GiftE": SRC_GIVENBYNPC,
               "ItemA": SRC_LAYINGAROUND,
               "Partner": SRC_GIVENBYNPC,
               "KootGift00": SRC_GIVENBYNPC,
               "KootGift01": SRC_GIVENBYNPC,
               "KootGift02": SRC_GIVENBYNPC,
               "KootGift03": SRC_GIVENBYNPC,
               "KootGift04": SRC_GIVENBYNPC,
               "KootGift05": SRC_GIVENBYNPC,
               "KootGift06": SRC_GIVENBYNPC,
               "KootGift07": SRC_GIVENBYNPC,
               "KootGift08": SRC_GIVENBYNPC,
               "KootGift09": SRC_GIVENBYNPC,
               "KootGift0A": SRC_GIVENBYNPC,
               "KootGift0B": SRC_GIVENBYNPC,
               "KootGift0C": SRC_GIVENBYNPC,
               "KootGift0D": SRC_GIVENBYNPC,
               "KootGift0E": SRC_GIVENBYNPC,
               "KootGift0F": SRC_GIVENBYNPC,
               "KootGift10": SRC_GIVENBYNPC,
               "KootGift11": SRC_GIVENBYNPC,
               "KootGift12": SRC_GIVENBYNPC,
               "KootGift13": SRC_GIVENBYNPC,},
    "NOK_03": {"ItemA": SRC_LAYINGAROUND,},
    "NOK_04": {"GiftA": SRC_DROPPEDBYENEMY,},
    "NOK_11": {"RBlockA": SRC_ITEMBLOCK,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},
    "NOK_12": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK},
    "NOK_13": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_LAYINGAROUND,
               "RBlockA": SRC_HIDDENBLOCK,},
    "NOK_14": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "ItemF": SRC_LAYINGAROUND,},
    "NOK_15": {"Tree1_Drop1A": SRC_HIDDENINTREE,},

# Koopa Bros. Fortress
    "TRD_00": {"ChestA": SRC_CHEST,
               "ChestB": SRC_CHEST,},
    "TRD_01": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_DROPPEDBYENEMY,},
    "TRD_03": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,},
    "TRD_06": {"Partner": SRC_GIVENBYNPC},
    "TRD_08": {"ItemA": SRC_LAYINGAROUND,},
    "TRD_09": {"YBlockA": SRC_ITEMBLOCK,},

# Mt Rugged
    "IWA_00": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_GIVENBYNPC,
               "YBlockA": SRC_ITEMBLOCK,},
    "IWA_01": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,},
    "IWA_02": {"GiftA": SRC_GIVENBYNPC,
               "ItemA": SRC_LAYINGAROUND,},
    "IWA_03": {"ChestA": SRC_CHEST,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "ItemF": SRC_LAYINGAROUND,
               "ItemG": SRC_LAYINGAROUND,
               "ItemH": SRC_LAYINGAROUND,
               "ItemI": SRC_LAYINGAROUND,
               "ItemJ": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,},
    "IWA_04": {"ItemA": SRC_LAYINGAROUND,},
    "IWA_10": {"Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush2_Drop1": SRC_HIDDENINBUSH,
               "Bush3_Drop1": SRC_HIDDENINBUSH,
               "Bush4_Drop1": SRC_HIDDENINBUSH,
               "Partner": SRC_GIVENBYNPC,
               "RandomBlockItemA": SRC_ITEMBLOCK},

# Dry Dry Outpost
    "DRO_01": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "Tree1_Drop1": SRC_HIDDENINTREE,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "DRO_02": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_LAYINGAROUND,},

# Dry Dry Desert
    "SBK_00": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},
    "SBK_02": {"GiftA": SRC_GIVENBYNPC,},
    "SBK_05": {"ItemA": SRC_LAYINGAROUND,},
    "SBK_06": {"Tree1_Drop1": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_10": {"HiddenYBlockA": SRC_HIDDENBLOCK,},
    "SBK_14": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_20": {"YBlockA": SRC_HIDDENBLOCK,
               "YBlockB": SRC_HIDDENBLOCK,
               "YBlockC": SRC_HIDDENBLOCK,},
    "SBK_22": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,
               "YBlockD": SRC_ITEMBLOCK,
               "YBlockE": SRC_ITEMBLOCK,},
    "SBK_24": {"HiddenRBlockA": SRC_HIDDENBLOCK,},
    "SBK_25": {"RandomBlockItemA": SRC_ITEMBLOCK,
               "RandomBlockItemB": SRC_ITEMBLOCK,},
    "SBK_26": {"Tree1_Drop1": SRC_HIDDENINTREE,},
    "SBK_30": {"Tree2_Drop1A": SRC_HIDDENINTREE,},
    "SBK_33": {"HiddenPanel": SRC_HIDDENTILE,},
    "SBK_34": {"GiftA": SRC_GIVENBYNPC,
               "Tree1_Drop1": SRC_HIDDENINTREE,},
    "SBK_35": {"Tree1_Drop1": SRC_HIDDENINTREE,},
    "SBK_36": {"Tree9_Drop1A": SRC_HIDDENINTREE,
               "Tree1_Drop1": SRC_HIDDENINTREE,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "Tree6_Drop1": SRC_HIDDENINTREE,},
    "SBK_40": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_43": {"YBlockA": SRC_ITEMBLOCK,},
    "SBK_45": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,},
    "SBK_46": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,
               "Tree2_Drop1": SRC_HIDDENINTREE,},
    "SBK_52": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_55": {"ItemA": SRC_LAYINGAROUND,
               "Tree1_Drop1": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_56": {"Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree2_Drop1A": SRC_HIDDENINTREE,
               "Tree3_Drop1": SRC_HIDDENINTREE,
               "Tree9_Drop1": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "SBK_61": {"HiddenRBlockA": SRC_HIDDENBLOCK,},
    "SBK_64": {"YBlockA": SRC_ITEMBLOCK,},
    "SBK_66": {"Tree3_Drop1": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,
               "RandomBlockItemB": SRC_ITEMBLOCK,
               "RandomBlockItemC": SRC_ITEMBLOCK,
               "RandomBlockItemD": SRC_ITEMBLOCK,
               "RandomBlockItemE": SRC_ITEMBLOCK,
               "RandomBlockItemF": SRC_ITEMBLOCK,},

# Dry Dry Ruins
    "ISK_02": {"ItemA": SRC_LAYINGAROUND,},
    "ISK_03": {"ItemA": SRC_LAYINGAROUND,},
    "ISK_05": {"ItemA": SRC_LAYINGAROUND,},
    "ISK_06": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,},
    "ISK_07": {"ItemA": SRC_DROPPEDBYENEMY,
               "ItemB": SRC_LAYINGAROUND,},
    "ISK_09": {"ChestA": SRC_CHEST,
               "BigChest": SRC_CHEST,},
    "ISK_10": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "ISK_12": {"ItemA": SRC_LAYINGAROUND,},
    "ISK_13": {"ItemA": SRC_LAYINGAROUND,},
    "ISK_14": {"ItemA": SRC_LAYINGAROUND,},

# Forever Forest
    "MIM_04": {"GiftA": SRC_GIVENBYNPC,},
    "MIM_08": {"RBlockA": SRC_ITEMBLOCK,},
    "MIM_09": {"RBlockA": SRC_ITEMBLOCK,},
    "MIM_11": {"Bush1_Drop1": SRC_HIDDENINBUSH,
               "YBlockA": SRC_ITEMBLOCK,},
    "MIM_12": {"HiddenPanel": SRC_HIDDENTILE,},

# Boo's Mansion
    "OBK_01": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,},
    "OBK_02": {"HiddenPanel": SRC_HIDDENTILE,},
    "OBK_03": {"CrateA": SRC_CRATE,
               "GiftA": SRC_GIVENBYNPC,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "OBK_04": {"CrateA": SRC_CRATE,
               "BigChest": SRC_CHEST,
               "HiddenPanel": SRC_HIDDENTILE,},
    "OBK_05": {"CrateA": SRC_CRATE,
               "CrateB": SRC_CRATE,},
    "OBK_06": {"CrateA": SRC_CRATE,
               "ItemA": SRC_LAYINGAROUND,},
    "OBK_07": {"ChestA": SRC_CHEST,},
    "OBK_08": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_GIVENBYNPC,},
    "OBK_09": {"Partner": SRC_GIVENBYNPC},

# Gusty Gulch
    "ARN_02": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,},
    "ARN_03": {"GiftA": SRC_GIVENBYNPC,
               "YBlockA": SRC_ITEMBLOCK,},
    "ARN_04": {"ItemA": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,},

# Tubba's Castle
    "DGB_03": {"ItemA": SRC_LAYINGAROUND,},
    "DGB_04": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "DGB_06": {"ChestA": SRC_CHEST,},
    "DGB_07": {"ItemA": SRC_LAYINGAROUND,},
    "DGB_11": {"ItemA": SRC_LAYINGAROUND,},
    "DGB_12": {"ChestA": SRC_CHEST,},
    "DGB_13": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "ItemF": SRC_LAYINGAROUND,
               "ItemG": SRC_LAYINGAROUND,},
    "DGB_14": {"YBlockA": SRC_ITEMBLOCK,},
    "DGB_16": {"ItemA": SRC_LAYINGAROUND,},

# Shy Guy's Toybox
    "OMO_01": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "ItemA": SRC_DROPPEDBYENEMY,
               "ItemB": SRC_DROPPEDBYENEMY,
               "ItemC": SRC_DROPPEDBYENEMY,
               "ItemD": SRC_DROPPEDBYENEMY,
               "ItemE": SRC_DROPPEDBYENEMY,
               "ItemF": SRC_DROPPEDBYENEMY,},
    "OMO_02": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "ItemA": SRC_LAYINGAROUND,
               "YBlockA": SRC_HIDDENBLOCK,},
    "OMO_03": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "OMO_04": {"ChestA": SRC_CHEST,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "ItemF": SRC_LAYINGAROUND,
               "ItemG": SRC_LAYINGAROUND,
               "ItemH": SRC_LAYINGAROUND,
               "ItemI": SRC_LAYINGAROUND,
               "ItemJ": SRC_LAYINGAROUND,
               "ItemK": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,},
    "OMO_05": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "ItemA": SRC_GIVENBYNPC,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},
    "OMO_06": {"ChestA": SRC_CHEST,
               "HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "OMO_07": {"ChestA": SRC_CHEST,
               "ChestB": SRC_CHEST,
               "ChestC": SRC_CHEST,
               "ItemA": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,},
    "OMO_08": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "OMO_09": {"ChestA": SRC_CHEST,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "ItemD": SRC_LAYINGAROUND,
               "ItemE": SRC_LAYINGAROUND,
               "ItemF": SRC_LAYINGAROUND,
               "ItemG": SRC_LAYINGAROUND,
               "ItemH": SRC_LAYINGAROUND,
               "ItemI": SRC_LAYINGAROUND,
               "ItemJ": SRC_LAYINGAROUND,
               "ItemK": SRC_LAYINGAROUND,
               "ItemL": SRC_LAYINGAROUND,
               "ItemM": SRC_LAYINGAROUND,
               "ItemN": SRC_LAYINGAROUND,
               "ItemO": SRC_DROPPEDBYENEMY,
               "RandomBlockItemA": SRC_ITEMBLOCK},
    "OMO_10": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "OMO_11": {"HiddenRBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,
               "RandomBlockItemB": SRC_ITEMBLOCK,},
    "OMO_12": {"Partner": SRC_GIVENBYNPC},
    "OMO_13": {"ChestA": SRC_CHEST,
               "HiddenYBlockA": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,},
    "OMO_17": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,
               "RandomBlockItemA": SRC_ITEMBLOCK,},

# Jade Jungle
    "JAN_00": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "Tree1_Drop1A": SRC_HIDDENINTREE,},
    "JAN_01": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,
               "ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "Tree3_Drop1": SRC_HIDDENINTREE,
               "Tree4_Drop1": SRC_HIDDENINTREE,
               "Tree5_Drop1": SRC_HIDDENINTREE,
               "Tree6_Drop1": SRC_HIDDENINTREE,
               "Tree7_Drop1A": SRC_HIDDENINTREE,
               "Tree7_Drop1B": SRC_HIDDENINTREE,},
    "JAN_02": {"GiftA": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "Tree2_Drop1A": SRC_HIDDENINTREE,
               "Tree3_Drop1A": SRC_HIDDENINTREE,},
    "JAN_03": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "GiftC": SRC_GIVENBYNPC,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "JAN_04": {"ChestA": SRC_CHEST,
               "ItemA": SRC_LAYINGAROUND,
               "Tree2_Drop1A": SRC_HIDDENINTREE,
               "Partner": SRC_GIVENBYNPC,},
    "JAN_05": {"RBlockA": SRC_ITEMBLOCK,
               "Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush2_Drop1": SRC_HIDDENINBUSH,
               "Tree2_Drop1": SRC_HIDDENINTREE,},
    "JAN_06": {"ItemA": SRC_UNDERWATER,
               "Tree1_Drop1": SRC_HIDDENINTREE,},
    "JAN_07": {"Tree1_Drop1": SRC_HIDDENINTREE,},
    "JAN_08": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "ItemA": SRC_UNDERWATER,
               "ItemB": SRC_UNDERWATER,
               "ItemC": SRC_UNDERWATER,
               "Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush2_Drop1": SRC_HIDDENINBUSH,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "Tree3_Drop1": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "JAN_09": {"Bush1_Drop1": SRC_HIDDENINBUSH,
               "Bush6_Drop1": SRC_HIDDENINBUSH,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "Tree3_Drop1": SRC_HIDDENINTREE,},
    "JAN_10": {"ItemA": SRC_UNDERWATER,},
    "JAN_12": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "Tree1_Drop1": SRC_HIDDENINVINES,
               "Tree1_Drop2": SRC_HIDDENINTREE,},
    "JAN_13": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "Tree1_Drop1": SRC_HIDDENINTREE,},
    "JAN_14": {"Tree2_Drop1": SRC_HIDDENINVINES,
               "Tree5_Drop1": SRC_HIDDENINVINES,},
    "JAN_15": {"HiddenPanel": SRC_HIDDENTILE,
               "Tree2_Drop1": SRC_HIDDENINTREE,},
    "JAN_18": {"ItemA": SRC_LAYINGAROUND,},
    "JAN_22": {"GiftA": SRC_GIVENBYNPC,
               "ItemA": SRC_LAYINGAROUND,},

# Mt Lavalava
    "KZN_03": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,
               "YBlockD": SRC_ITEMBLOCK,},
    "KZN_04": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "KZN_06": {"HiddenYBlockA": SRC_HIDDENBLOCK,},
    "KZN_07": {"BigChest": SRC_CHEST,},
    "KZN_08": {"ChestA": SRC_CHEST,},
    "KZN_09": {"HiddenPanel": SRC_HIDDENTILE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "KZN_18": {"HiddenPanel": SRC_HIDDENTILE,},
    "KZN_19": {"YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,},

# Flower Fields
    "FLO_03": {"GiftA": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree1_Drop1B": SRC_HIDDENINTREE,},
    "FLO_07": {"GiftA": SRC_GIVENBYNPC,
               "ItemA": SRC_GIVENBYNPC,},
    "FLO_08": {"ItemA": SRC_HIDDENINVINES,
               "ItemB": SRC_LAYINGAROUND,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree1_Drop1B": SRC_HIDDENINTREE,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "FLO_09": {"Tree1_Drop1": SRC_HIDDENINTREE,
               "ItemA": SRC_HIDDENINVINES,},
    "FLO_10": {"GiftA": SRC_GIVENBYNPC,
               "Tree1_Drop1A": SRC_HIDDENINTREE,},
    "FLO_11": {"RandomBlockItemA": SRC_ITEMBLOCK,},
    "FLO_12": {"GiftA": SRC_GIVENBYNPC,},
    "FLO_13": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "Partner": SRC_GIVENBYNPC,},
    "FLO_14": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_HIDDENINVINES,},
    "FLO_16": {"ItemA": SRC_GROUNDPOUND,
               "ItemB": SRC_HIDDENINVINES,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "FLO_17": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "ItemA": SRC_LAYINGAROUND,},
    "FLO_19": {"ItemA": SRC_LAYINGAROUND,},
    "FLO_22": {"ItemA": SRC_GIVENBYNPC,},
    "FLO_23": {"HiddenYBlockA": SRC_HIDDENBLOCK,
               "HiddenYBlockB": SRC_HIDDENBLOCK,},
    "FLO_24": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree1_Drop1B": SRC_HIDDENINTREE,
               "YBlockA": SRC_ITEMBLOCK,},
    "FLO_25": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_HIDDENINVINES,
               "Tree1_Drop1A": SRC_HIDDENINTREE,
               "Tree1_Drop1B": SRC_HIDDENINTREE,},

# Shiver Mountain
    "SAM_01": {"ChestA": SRC_CHEST,
               "GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,
               "HiddenPanel": SRC_HIDDENTILE,},
    "SAM_02": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_GIVENBYNPC,
               "ItemC": SRC_GIVENBYNPC,
               "ItemD": SRC_GIVENBYNPC,
               "ItemE": SRC_GIVENBYNPC,
               "ItemF": SRC_GIVENBYNPC,
               "ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "SAM_04": {"HiddenPanel": SRC_HIDDENTILE,
               "Tree2_Drop1": SRC_HIDDENINTREE,
               "ItemA": SRC_LAYINGAROUND,},
    "SAM_05": {"HiddenPanel": SRC_HIDDENTILE,
               "ItemA": SRC_LAYINGAROUND,
               "HiddenYBlockA": SRC_HIDDENBLOCK},
    "SAM_06": {"GiftA": SRC_GIVENBYNPC,
               "GiftB": SRC_GIVENBYNPC,},
    "SAM_07": {"HiddenYBlockA": SRC_HIDDENBLOCK,},
    "SAM_08": {"ItemA": SRC_LAYINGAROUND,
               "RandomBlockItemA": SRC_ITEMBLOCK,},
    "SAM_09": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,
               "ItemC": SRC_LAYINGAROUND},
    "SAM_10": {"ItemA": SRC_LAYINGAROUND,
               "RBlockA": SRC_ITEMBLOCK,},
    "SAM_11": {"ItemA": SRC_UNDERWATER,},
    "SAM_12": {"ItemA": SRC_LAYINGAROUND,},

# Crystal Palace
    "PRA_04": {"YBlockA": SRC_ITEMBLOCK,},
    "PRA_05": {"ChestA": SRC_CHEST,},
    "PRA_06": {"ItemA": SRC_LAYINGAROUND,},
    "PRA_11": {"ChestA": SRC_CHEST,},
    "PRA_12": {"ChestA": SRC_CHEST,},
    "PRA_14": {"RandomBlockItemA": SRC_ITEMBLOCK,
               "RandomBlockItemB": SRC_ITEMBLOCK,},
    "PRA_15": {"ItemA": SRC_LAYINGAROUND,},
    "PRA_21": {"HiddenPanel": SRC_HIDDENTILE,
               "YBlockA": SRC_ITEMBLOCK,},
    "PRA_22": {"HiddenPanel": SRC_HIDDENTILE,
               "HiddenYBlockA": SRC_HIDDENBLOCK,},
    "PRA_27": {"ChestA": SRC_CHEST,},
    "PRA_28": {"ChestA": SRC_CHEST,},
    "PRA_35": {"ChestA": SRC_CHEST,},

# Bowser's Castle
    "KPA_01": {"YBlockA": SRC_ITEMBLOCK,},
    "KPA_03": {"YBlockA": SRC_ITEMBLOCK,},
    "KPA_10": {"YBlockA": SRC_ITEMBLOCK,},
    "KPA_11": {"ItemA": SRC_DROPPEDBYENEMY,},
    "KPA_14": {"ItemA": SRC_LAYINGAROUND,
               "ItemB": SRC_LAYINGAROUND,},
    "KPA_15": {"ChestA": SRC_CHEST,},
    "KPA_17": {"CrateA": SRC_CRATE,
               "CrateB": SRC_CRATE,},
    "KPA_61": {"ItemA": SRC_LAYINGAROUND,
               "YBlockA": SRC_ITEMBLOCK,
               "YBlockB": SRC_ITEMBLOCK,
               "YBlockC": SRC_ITEMBLOCK,},
    "KPA_62": {"RBlockA": SRC_ITEMBLOCK,},
    "KPA_91": {"ItemA": SRC_DROPPEDBYENEMY,},
    "KPA_95": {"ItemA": SRC_DROPPEDBYENEMY,},
    "KPA_96": {"ShopItemA": SRC_SOLDBYNPC,
               "ShopItemB": SRC_SOLDBYNPC,
               "ShopItemC": SRC_SOLDBYNPC,
               "ShopItemD": SRC_SOLDBYNPC,
               "ShopItemE": SRC_SOLDBYNPC,
               "ShopItemF": SRC_SOLDBYNPC,},
    "KPA_100":{"ItemA": SRC_LAYINGAROUND,},
    "KPA_101":{"ItemA": SRC_LAYINGAROUND,},
    "KPA_111":{"HiddenYBlockA": SRC_HIDDENBLOCK,
               "YBlockA": SRC_ITEMBLOCK,},
    "KPA_119":{"ItemA": SRC_LAYINGAROUND,},
    "KPA_133":{"ItemA": SRC_LAYINGAROUND,},
    "KPA_134":{"HiddenYBlockA": SRC_HIDDENBLOCK,},

# Peach's Castle Grounds
    "OSR_01": {"GiftA": SRC_GIVENBYNPC,},
    "OSR_02": {"HiddenYBlockA": SRC_HIDDENBLOCK,},
}