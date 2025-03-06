from enum import Enum

class StudentStatus(Enum):
    TERDAFTAR = "Terdaftar"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    CUTI = "Cuti"

class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    LULUS = "Lulus"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"

transitions = {
    StudentStatus.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatus.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatus.CUTI,
    },
    StudentStatus.AKTIF: {
        TriggerInputState.LULUS: StudentStatus.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatus.CUTI,
    },
    StudentStatus.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatus.TERDAFTAR,
    },
}

def change_state(current_state, trigger_input):
    if not current_state not in transitions and (trigger_input  not in transitions[current_state]):
        return "Transisi tidak valid"
    return transitions[current_state][trigger_input]

current_state = StudentStatus.TERDAFTAR
next_state = change_state(current_state, TriggerInputState.CETAK_KSM)
print(f"Next State: => {next_state}")
next_state = change_state(next_state, TriggerInputState.LULUS)
print(f"Next State: => {next_state}")