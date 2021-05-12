# -*- coding: utf-8 -*-
"""
This code runs the "Flanker Task" experiment, where the participant is 
presented with one of 3 types of stimuli:   
CONGRUENT: >>>>> or <<<<<
INCONGRUENT: <<><< or >><>>
NEUTRAL: ||<|| or ||>||
The participant clicks the arrow keys (RIGHT or LEFT) corresponding to
the arrow presented in the MIDDLE of the stimulus, regardless of the 
surrounding symbols/arrows.
"""

import expyriment
from expyriment import misc

# Set up number of trials per block (the number of stimuli), and the number of blocks
n_trials_block = 6
n_blocks = 6

# Set trial length
duration = 2000

# Set up left and right arrow keys for participant responses
response_keys = [misc.constants.K_LEFT, misc.constants.K_RIGHT]

# Create stimuli
stimuli = ["<<<<<", ">>>>>", "||>||", "||<||", "<<><<", ">><>>"]

instructions = "Hello, and welcome to this experiment! \n \
                \nPlease read these instructions carefully:\n \
                \nKeep your eyes fixed on the cross in the middle of the screen.\n \
                Press the LEFT ARROW on your keyboard when you see the left-pointing arrow (<) in the center.\n \
                Press the RIGHT ARROW on your keyboard when you see the right-pointing arrow (>) in the center. \n \
                \nFocus on the CENTER arrow - try to IGNORE the surrounding arrows/symbols. \n \
                \nYou will do the task 6 times, with short breaks between each block. \n\
                \nPress the SPACEBAR to start the experiment."
                
experiment = expyriment.design.Experiment(name="Flanker Task")

expyriment.control.initialize(experiment)

# Set up experiment blocks and stimuli to be presented to the participant
for block in range(n_blocks):  
   
    temp_block = expyriment.design.Block(name=str(block + 1))
   
    for trials in range(n_trials_block):
        curr_stim = stimuli [trials]
        
        temp_stim = expyriment.stimuli.TextLine(text=curr_stim, text_size=60)
        
        temp_trial = expyriment.design.Trial()
        
        temp_trial.add_stimulus(temp_stim)

        # Set up trial types (based on type of stimulus)
        if trials <= 1:
            trialtype = 'congruent'
        
        elif trials == 2:
            trialtype = 'neutral'
        
        elif trials == 3:
            trialtype = 'neutral'
 
        elif trials >3:
            trialtype = 'incongruent'
        
        # Set up which keyboard responses are registered as correct for each stimulus
        if curr_stim[2] == '<':
            correctresponse = misc.constants.K_LEFT
 
        elif curr_stim[2] == '>':
            correctresponse = misc.constants.K_RIGHT
 
        temp_trial.set_factor('trialtype', trialtype)
        temp_trial.set_factor('correctresponse', correctresponse)
 
        temp_block.add_trial(temp_trial)
    
    # Randomize the order of trials within each block
    temp_block.shuffle_trials()
    experiment.add_block(temp_block)

# Name the variables to be recorded for each participant    
experiment.data_variable_names = ["Block", "Trial Type", "Correct Response", "Subject Response", 
                                  "Trial Number","RT", "Accuracy"]

# Begin presentation of the experiment to the participant
expyriment.control.start(skip_ready_screen=True)

fixation_cross = expyriment.stimuli.FixCross()
fixation_cross.preload()

expyriment.stimuli.TextScreen('Flanker Task', instructions).present()
experiment.keyboard.wait(expyriment.misc.constants.K_SPACE)

for block in experiment.blocks:
 
    for trial in block.trials:
 
        fixation_cross.present()

        trial.stimuli[0].preload()
        
        experiment.clock.wait(duration)

        trial.stimuli[0].present()

        experiment.clock.reset_stopwatch()
 
        # Collect participant's response and RT
        key, rt = experiment.keyboard.wait(keys=[expyriment.misc.constants.K_LEFT, 
                                            expyriment.misc.constants.K_RIGHT],
                                            duration = duration)
        
        experiment.clock.wait(duration - experiment.clock.stopwatch_time)
        
        # Collect participant's response accuracy
        if key == trial.get_factor('correctresponse'):
            acc = 1

        else:
            acc = 0
        
        # Collect data for participant (with RT and accuracy outlined above) 
        experiment.data.add([block.name, trial.get_factor('trialtype'),
                             trial.get_factor('correctresponse'),
                             key, trial.id, rt, acc])
    
    # Short message between blocks to remind participant how much of the experiment remains
    if block.name != '6':
        expyriment.stimuli.TextScreen('BREAK', 'That was block: '
                                      + block.name +
                                      ". \n Get ready for the next block!",
                                      ).present()
        experiment.clock.wait(4000)
 
# End experiment & display a thank you message to participant
expyriment.control.end(goodbye_text="Thank you very much for your contribution!",
                        goodbye_delay=4000)


