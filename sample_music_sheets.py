saaloony_elnas = """RE RE RE    RE RE RE    RE RE RE    RE RE RE RE
RE LA SOL LA    FA SOL  LA SI LA SI
SOL LA SOL LA   FA SOL SOL  ::  RE LA SOL LA    FA SOL  LA SI LA SI    ::   SOL SOL FA SOL FA FA MI MI RE RE
DO LA SI SOL LA FA SOL MI"""

saaloony_elnas = [n for n in saaloony_elnas.split() if n is not "::"]


ramsis_kasis_lesson5 = """RE MI Fa MI RE MI RE :: DO RE MI Fa MI :: DO RE MI RE DO SI LA :: Fa MI RE MI RE ::

La La La La Si La So :: Do Si Re Do Si La ::

Si La So La So Fa :: So Fa MI RE DO RE MI Fa :: La So Fa So Fa MI :: Fa MI RE DO SI DO RE

MI        Fa Sol :: Fa MI                   :: MI MI MI Fa Sol :: Fa MI

MI      Fa      Sol     La          Si      La      Sol     Fa     ::   La      Sol       Fa        MI

Si  Si    Si  Sol    Fa   MI    ::    Mi Do Si La      Sol       :: Mi Do Si La   RE MI Fa Sol"""

ramsis_kasis = [n for n in ramsis_kasis_lesson5.split() if n is not "::"]