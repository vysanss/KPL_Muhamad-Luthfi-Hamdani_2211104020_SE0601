from enum import Enum
import time

class TrafficLight(Enum):
    MERAH = "Merah"
    KUNING = "Kuning"
    HIJAU = "Hijau"

state_transitions = {
    TrafficLight.MERAH: TrafficLight.KUNING,
    TrafficLight.KUNING: TrafficLight.HIJAU,
    TrafficLight.HIJAU: TrafficLight.MERAH
}

state_duration = {
    TrafficLight.MERAH: 5,
    TrafficLight.KUNING: 2,
    TrafficLight.HIJAU: 5
}

current_state = TrafficLight.MERAH
# next_state = state_transitions[current_state]
# print(f"next_state: {next_state}")

while True:
    print(f"Lampu: {current_state.value} ({state_duration[current_state]} detik)")
    time.sleep(state_duration[current_state])
    current_state = state_transitions[current_state]
    print(f"Next State: {current_state.value}")
    print("")
