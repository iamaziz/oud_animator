# source: https://www.youtube.com/watch?v=tsjgCaa_6ek
saaloony_elnas = """RE RE RE    RE RE RE    RE RE RE    RE RE RE RE
RE La Sol La    Fa Sol  La Si La Si
Sol La Sol La   Fa Sol Sol  ::  RE La Sol La    Fa Sol  La Si La Si    ::   Sol Sol Fa Sol Fa Fa Mi Mi RE RE
Do La Si Sol La Fa Sol Mi"""

saaloony_elnas = [n for n in saaloony_elnas.split() if n is not "::"]



# source: https://www.youtube.com/watch?v=pmHqqD35r-E 
ramsis_kasis_lesson5 = """RE MI Fa MI RE MI RE :: DO RE MI Fa MI :: DO RE MI RE DO SI LA :: Fa MI RE MI RE ::

La La La La Si La Sol :: Do Si Re Do Si La ::

Si La So La Sol Fa :: Sol Fa MI RE DO RE MI Fa :: La Sol Fa Sol Fa MI :: Fa MI RE DO SI DO RE

MI        Fa Sol :: Fa MI                   :: MI MI MI Fa Sol :: Fa MI

MI      Fa      Sol     La          Si      La      Sol     Fa     ::   La      Sol       Fa        MI

Si  Si    Si  Sol    Fa   MI    ::    Mi Do Si La      Sol       :: Mi Do Si La   RE MI Fa Sol"""

ramsis_kasis = [n for n in ramsis_kasis_lesson5.split() if n is not "::"]