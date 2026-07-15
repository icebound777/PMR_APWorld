from typing import Dict
import dataclasses

from typing_extensions import override

#from BaseClasses import CollectionState
from rule_builder.rules import (
    #And,
    #Or,
    #AtLeast,
    True_,
    #False_,
    Has,
    #HasAll,
    #HasAny,
    HasAllCounts,
    #HasAnyCount,
    #HasFromList,
    #HasFromListUnique,
    #HasGroup,
    #HasGroupUnique,
    #CanReachLocation,
    #CanReachRegion,
    #CanReachEntrance,
    Rule,
    OptionFilter,
)

from ...options import HiddenBlockMode

# Gear Helper Rules

@dataclasses.dataclass()
class HasHammer(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Hammer": 1}).resolve(world)

@dataclasses.dataclass()
class HasSuperHammer(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Hammer": 2}).resolve(world)

@dataclasses.dataclass()
class HasUltraHammer(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Hammer": 3}).resolve(world)

@dataclasses.dataclass()
class HasBoots(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Boots": 1}).resolve(world)

@dataclasses.dataclass()
class HasSuperBoots(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Boots": 2}).resolve(world)

@dataclasses.dataclass()
class HasUltraBoots(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return HasAllCounts({"Progressive Boots": 3}).resolve(world)

# General World Interaction

@dataclasses.dataclass()
class CanFlipPanels(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (HasUltraHammer() | HasSuperBoots()).resolve(world)

@dataclasses.dataclass()
class CanShakeTrees(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (Has("Bombette") | HasHammer()).resolve(world)

@dataclasses.dataclass()
class CanSeeHiddenBlocks(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return CanUseAbilityWatt(
            options=[OptionFilter(
                HiddenBlockMode,
                HiddenBlockMode.option_Always_Visible,
                operator="lt",
            )],
            filtered_resolution=True,
        ).resolve(world)

### Partner Abilities

@dataclasses.dataclass()
class CanUseAbilityKooper(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Kooper").resolve(world)

@dataclasses.dataclass()
class CanUseAbilityBombette(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Bombette").resolve(world)

@dataclasses.dataclass()
class CanUseAbilityParakarry(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Parakarry").resolve(world)

@dataclasses.dataclass()
class CanUseAbilityBow(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Bow").resolve(world)

@dataclasses.dataclass()
class CanUseAbilityWatt(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Watt").resolve(world)

@dataclasses.dataclass()
class CanUseAbilitySushie(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Sushie").resolve(world)

@dataclasses.dataclass()
class CanUseAbilityLakilester(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        if world.options.partners_always_usable.value:
            return True_().resolve(world)
        else:
            return Has("Lakilester").resolve(world)

### Multiple Solutions to the task

@dataclasses.dataclass()
class CanHitGroundedBlocks(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (
            CanUseAbilityKooper()
            | CanUseAbilityBombette()
            | HasSuperBoots()
            | HasHammer()
        ).resolve(world)

@dataclasses.dataclass()
class CanHitFloatingBlocks(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (CanUseAbilityKooper() | HasBoots()).resolve(world)

@dataclasses.dataclass()
class CanHitGroundedSwitches(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (
            CanUseAbilityKooper()
            | CanUseAbilityBombette()
            | CanUseAbilityParakarry()
            | HasBoots()
            | HasHammer()
        ).resolve(world)

@dataclasses.dataclass()
class CanClimbSteps(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (CanUseAbilityParakarry() | HasBoots()).resolve(world)

@dataclasses.dataclass()
class CanReenterVerticalPipes(Rule["PaperMarioWorld"], game="Paper Mario"):
    @override
    def _instantiate(self, world) -> Rule.Resolved:
        return (
            CanUseAbilityKooper()
            | CanUseAbilityParakarry()
            | HasBoots()
        ).resolve(world)



logichelpers: Dict[str, Rule] = {
    "Boots": "(Progressive_Boots, 1)",
    "Super_Boots": "(Progressive_Boots, 2)",
    "Ultra_Boots": "(Progressive_Boots, 3)",
    "Hammer": "(Progressive_Hammer, 1)",
    "Super_Hammer": "(Progressive_Hammer, 2)",
    "Ultra_Hammer": "(Progressive_Hammer, 3)",

    "can_flip_panels": "Ultra_Hammer or Super_Boots",

    "can_shake_trees": "Bombette or Hammer",

    "can_hit_grounded_blocks": "can_use_ability_bombette or can_use_ability_kooper or Super_Boots or Hammer",
    "can_hit_floating_blocks": "can_use_ability_kooper or Boots",
    "can_hit_grounded_switches": "can_use_ability_bombette or can_use_ability_kooper or Boots or Hammer or can_use_ability_parakarry",

    "can_climb_steps": "Boots or can_use_ability_parakarry",
    "saved_all_yoshi_kids": "'RF_SavedYoshiKid_1' and 'RF_SavedYoshiKid_2' and 'RF_SavedYoshiKid_3' and 'RF_SavedYoshiKid_4' and 'RF_SavedYoshiKid_5'",
    "can_reenter_vertical_pipes": "can_use_ability_kooper or Boots or can_use_ability_parakarry",

    "has_strong_aerial_partner": "Bow or Watt or Sushie or Lakilester",
    "has_weak_aerial_partner": "Goombario or Parakarry",

    "can_pass_kent": "(not kent_c_koopa == 1) or (('STARSPIRIT', 2) and (Boots or Goombario))",
    "can_beat_all_bloopers": "(can_beat_blooper and can_beat_electro_blooper and can_beat_super_blooper)",
    "can_beat_blooper": "(Super_Boots or (Boots and has_weak_aerial_partner) or has_strong_aerial_partner) or blooper_damage_requirements < 1",
    "can_beat_electro_blooper": "(Ultra_Boots or (Super_Boots and (has_strong_aerial_partner or has_weak_aerial_partner))) or blooper_damage_requirements < 2",
    "can_beat_super_blooper": "(Ultra_Boots and has_strong_aerial_partner) or blooper_damage_requirements < 3",

    "can_see_hidden_blocks": "can_use_ability_watt or hidden_block_mode == 3",

    "has_required_spirits": "('STARSPIRIT_1' or 1 not in required_spirits) and ('STARSPIRIT_2' or 2 not in required_spirits) and ('STARSPIRIT_3' or 3 not in required_spirits) and ('STARSPIRIT_4' or 4 not in required_spirits) and ('STARSPIRIT_5' or 5 not in required_spirits) and ('STARSPIRIT_6' or 6 not in required_spirits) and ('STARSPIRIT_7' or 7 not in required_spirits)",

    "star_way_star_spirits": "('STARSPIRIT', star_way_spirits)",
    "star_way_power_stars": "(Power_Star, star_way_power_stars) or not power_star_hunt",
    "star_way_specific_spirits": "has_required_spirits or not require_specific_spirits",
    "can_reach_star_way": "star_way_star_spirits and star_way_power_stars and star_way_specific_spirits",
    "star_way_goal": "seed_goal == 1",

    "star_beam_power_stars": "(Power_Star, star_beam_power_stars) or not power_star_hunt",
    "star_beam_star_spirits": "('STARSPIRIT', star_beam_spirits)",
    "has_star_beam_requirements": "star_beam_star_spirits and star_beam_power_stars",

    "can_use_ability_kooper": "Kooper or partners_always_usable",
    "can_use_ability_bombette": "Bombette or partners_always_usable",
    "can_use_ability_parakarry": "Parakarry or partners_always_usable",
    "can_use_ability_bow": "Bow or partners_always_usable",
    "can_use_ability_watt": "Watt or partners_always_usable",
    "can_use_ability_sushie": "Sushie or partners_always_usable",
    "can_use_ability_lakilester": "Lakilester or partners_always_usable"
}