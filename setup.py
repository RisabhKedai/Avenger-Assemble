import cx_Freeze

executables = [cx_Freeze.Executable("C:/Users/Lenovo/Desktop/mygame/Avenger.py",base="Win32GUI",icon="data/iconga.ico")]

cx_Freeze.setup(
    name="AVENGER",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["data/images.bmp",
                                            "data/thanos.bmp",
                                            'data/iconga.ico'
                                           ]}},
    executables = executables


    )




'''
"C:/Users/Lenovo/Desktop/mygame/button.py",
"C:/Users/Lenovo/Desktop/mygame/game_func.py",
"C:/Users/Lenovo/Desktop/mygame/game_stats.py",
"C:/Users/Lenovo/Desktop/mygame/bullets.py",
"C:/Users/Lenovo/Desktop/mygame/settings.py",
"C:/Users/Lenovo/Desktop/mygame/ironman.py",
"C:/Users/Lenovo/Desktop/mygame/scoreboard.py",
"C:/Users/Lenovo/Desktop/mygame/thanos.py"
'''
