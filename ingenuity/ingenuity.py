from treedict import TreeDict

def output_location(state):

    if state['location', 'previous'] != state['location', 'current']:
        print(state['location', 'current'])
        state['location', 'previous'] = state['location', 'current']

def main():

    state = TreeDict({ 'location': { 'current': 'hab'}})

    while True:

        output_location(state)

        cmd = input(':')

        if cmd == 'go airlock':
            state['location', 'current'] = 'airlock'

if __name__ == '__main__':
    main()