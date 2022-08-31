#! /usr/bin/env python
# updated: <2016-02-04 Esther LIN>
# -*- coding: utf-8 -*-

from expyriment import design, control, stimuli, io, misc

AUDIO = 'wav/ch23-25.wav'

exp = design.Experiment(name="Le_Petit_Prince")

control.set_develop_mode(False)
control.defaults.open_gl = 2

##
control.initialize(exp)

stim = stimuli.Audio(AUDIO)

fixcrossGreen = stimuli.FixCross(size=(45, 45), line_width=5,
                                 colour=(0, 255, 0))
fixcrossGreen.preload()
fixcrossGrey = stimuli.FixCross(size=(45, 45), line_width=3,
                                colour=(192, 192, 192))
fixcrossGrey.preload()


def clear_screen():
    exp.screen.clear()
    exp.screen.update()

def wait_for_MRI_synchro():
    fixcrossGreen.present(clear=True, update=True)
    exp.keyboard.wait_char('t')

control.start(exp)

stim.preload()
wait_for_MRI_synchro()
clear_screen()
fixcrossGrey.present(clear=True, update=True)
stim.present()
control.wait_end_audiosystem()
io.Keyboard.process_control_keys()

control.end()
