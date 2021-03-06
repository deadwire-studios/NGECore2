import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('heroic_tusken_flight_crew')
	mobileTemplate.setLevel(90)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("heroic mos espa citizien")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(True)
	mobileTemplate.setOptionsBitmask(128)
	
	templates = Vector()
	templates.add('object/mobile/shared_miner_pilot.iff')
	templates.add('object/mobile/shared_space_newbie_generic_pilot_male_01.iff')
	templates.add('object/mobile/shared_dressed_royal_pilot_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_royal_pilot_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_bth_spynet_pilot_f_01.iff')
	templates.add('object/mobile/shared_dressed_bth_spynet_pilot_m_02.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/pistol/shared_pistol_scout_blaster.iff', WeaponType.PISTOL, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('heroic_tusken_flight_crew', mobileTemplate)
	return