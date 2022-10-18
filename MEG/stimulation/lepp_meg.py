#! /usr/bin/env python
# updated: <2022-10-18 Corentin BEL>
# -*- coding: utf-8 -*-

from expyriment import design, control, stimuli, io, misc

import meg_triggers

import sys

initialized = False

#AUDIO = 'wav/ch1-3.wav'

run = int(sys.argv[1])


dict_i_chapt = {1: '1-3',2:'4-6',3:'7-9',4:'10-12',5:'13-14',6:'15:19',7:'20-22',8:'23-25',9:'26-27'}

AUDIO = f'wav/{run}_ch{dict_i_chapt[run]}_clicks.wav'##'wav/ch1-3.wav'


print(f'\n Ready to play {AUDIO} \n')
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
#wait_for_MRI_synchro()
p1 = meg_triggers.send_start(initialized)
initialized = True # to not have to recreate the parport
exp.clock.wait(50)
meg_triggers.send_stop(p1)

clear_screen()
fixcrossGrey.present(clear=True, update=True)
stim.present()
control.wait_end_audiosystem()

p1 = meg_triggers.send_start(initialized,p1)
exp.clock.wait(50)
meg_triggers.send_stop(p1)

io.Keyboard.process_control_keys()

control.end()
