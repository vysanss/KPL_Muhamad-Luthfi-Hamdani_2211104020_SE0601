class FSM:
    def __init__(self, initial_state, transitions):
        self.state = initial_state
        self.transitions = transitions

    def on_event(self, event):
        if event in self.transitions[self.state]:
            self.state = self.transitions[self.state][event]
        return self.state

if __name__ == "__main__":

    transitions = {
        'idle': {'card_inserted': 'card_inserted'},
        'card_inserted': {'pin_entered': 'pin_verified', 'card_removed': 'idle'},
        'pin_verified': {'transaction_selected': 'transaction_in_progress', 'card_removed': 'idle'},
        'transaction_in_progress': {'transaction_completed': 'idle', 'card_removed': 'idle'},
    }

    # Create the FSM instance
    fsm = FSM('idle', transitions)

    # Simulate ATM events
    print(fsm.on_event('card_inserted'))  # Output: card_inserted
    print(fsm.on_event('pin_entered'))    # Output: pin_verified
    print(fsm.on_event('transaction_selected'))  # Output: transaction_in_progress
    print(fsm.on_event('transaction_completed'))  # Output: idle
    print(fsm.on_event('card_inserted'))  # Output: card_inserted
    print(fsm.on_event('card_removed'))   # Output: idle
