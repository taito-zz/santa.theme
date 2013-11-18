PROFILE_ID = 'profile-santa.theme:default'


def reimport_viewlets(setup):
    """Reimport viewlets"""
    setup.runImportStepFromProfile(PROFILE_ID, 'viewlets', run_dependencies=False, purge_old=False)
