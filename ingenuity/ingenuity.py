from treedict import TreeDict

def wordwrap(paragraph):

    words = paragraph.split()
    line = ''
    for word in words:
        if (len(line) + len(word) > 59):
            yield line
            line = word
        else:
            line = word if line == '' else line + ' ' + word

    yield line

def output_location(location, state):

    current = state['location', 'current']
    previous = state['location', 'previous']

    if current != previous:

        for paragraph in location[current,'description']:
            for line in wordwrap(paragraph):
                print(line)
            print()

        state['location', 'previous'] = current

def question_asked(location, state, cmd):

    current = state['location', 'current']
    questions = location[current, 'questions']

    if cmd in questions:
        answer = location[current,'questions', cmd]
        for line in wordwrap(answer):
            print(line)
        print()

def main():

    # oxygen toxicity sudden convulsions and unconsciousness
    state = { 'location': { 'current': 'wake up'},
              'suit': { 'pressure': 'normal',
                        'co2 absorbers': 'expended',
                        'mode': 'blood letting',
                        'nitrogen': 'empty',
                        'oxygen': 15,
                        'oxygen content': 80,
                        'status': 'breach'},
              'breach kit': {}
              }

    #http://www.readanybook.com/online/565265
    location = {
        'wake up': {
            'description': [
                'You awake to the oxygen alarm in your suit. A steady, obnoxious beeping that '
                'eventually rouses you from a deep and profound desire to just fucking die.',
                'You are facedown, almost totally buried in sand. As you groggily came to, you '
                'wonder why you aren\'t more dead.'],
            'questions': {
                'where':
                    'You have been knocked back quite a ways and rolled down a steep hill.',
                'what':
                    'Your main communications dish, which relayed signals from the Hab to '
                    'Hermes, acted like a parachute, getting torn from its foundation and carried '
                    'with the torrent. Along the way, it crashed through the reception antenna '
                    'array. Then one of those long thin antennae slammed into you end-first. It '
                    'tore through your suit like a bullet through butter, and you felt the worst '
                    'pain of your life as it ripped open your side.',
                'last':
                    'You vaguely remember having '
                    'the wind knocked out of you (pulled out of you, really) and your ears popping '
                    'painfully as the pressure of your suit escaped.' }},
        'look around': [
            'The antenna had enough force to punch through the suit and my side, but it had been stopped by my pelvis. So there was only one hole in the suit (and a hole in me, of course).',
            'I had been knocked back quite a ways and rolled down a steep hill. Somehow I landed facedown, which forced the antenna to a strongly oblique angle that put a lot of torque on the hole in the suit. It made a weak seal.'],
        'check hole': [
            'Then, the copious blood from my wound trickled down toward the hole. As the blood reached the site of the breach, the water in it quickly evaporated from the airflow and low pressure, leaving a gunky residue behind. More blood came in behind it and was also reduced to gunk. Eventually, it sealed the gaps around the hole and reduced the leak to something the suit could counteract.'],
        'check suit': [
            'The suit did its job admirably. Sensing the drop in pressure, it constantly flooded itself with air from my nitrogen tank to equalize. Once the leak became manageable, it only had to trickle new air in slowly to relieve the air lost.',
            'After a while, the CO2 (carbon dioxide) absorbers in the suit were expended. That\'s really the limiting factor to life support. Not the amount of oxygen you bring with you, but the amount of CO2 you can remove. In the Hab, I have the oxygenator, a large piece of equipment that breaks apart CO2 to give the oxygen back. But the space suits have to be portable, so they use a simple chemical absorption process with expendable filters. I\'d been asleep long enough that my filters were useless.',
            'The suit saw this problem and moved into an emergency mode the engineers call \'bloodletting.\' Having no way to separate out the CO2, the suit deliberately vented air to the Martian atmosphere, then backfilled with nitrogen. Between the breach and the bloodletting, it quickly ran out of nitrogen. All it had left was my oxygen tank.'
            'So it did the only thing it could to keep me alive. It started backfilling with pure oxygen. I now risked dying from oxygen toxicity, as the excessively high amount of oxygen threatened to burn up my nervous system, lungs, and eyes. An ironic death for someone with a leaky space suit: too much oxygen.',
            'Every step of the way would have had beeping alarms, alerts, and warnings. But it was the high-oxygen warning that woke me.',
            'The sheer volume of training for a space mission is astounding. I\'d spent a week back on Earth practicing emergency space suit drills. I knew what to do.',
            'Carefully reaching to the side of my helmet, I got the breach kit. It\'s nothing more than a funnel with a valve at the small end and an unbelievably sticky resin on the wide end. The idea is you have the valve open and stick the wide end over a hole. The air can escape through the valve, so it doesn\'t interfere with the resin making a good seal. Then you close the valve, and you\'ve sealed the breach.',
            'The tricky part was getting the antenna out of the way. I pulled it out as fast as I could, wincing as the sudden pressure drop dizzied me and made the wound in my side scream in agony.',
            'I got the breach kit over the hole and sealed it. It held. The suit backfilled the missing air with yet more oxygen. Checking my arm readouts, I saw the suit was now at 85 percent oxygen. For reference, Earth\'s atmosphere is about 21 percent. I\'d be okay, so long as I didn\'t spend too much time like that.',
            'I stumbled up the hill back toward the Hab. As I crested the rise, I saw something that made me very happy and something that made me very sad: The Hab was intact (yay!) and the MAV was gone (boo!).']}

    while True:

        output_location(TreeDict(location), TreeDict(state))

        cmd = input(':')

        question_asked(TreeDict(location), TreeDict(state), cmd)

if __name__ == '__main__':
    main()