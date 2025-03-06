from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(nama: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis Kelamin itu harus PRIA atau WANITA")
    
    patients.append({"name": nama,"gender": gender})
    print(f"Berhasil menambahkan pasien {nama} dengan jenis kelamin {gender.name}")

add_patient("Budi", JenisKelamin.PRIA)
add_patient("Siti", JenisKelamin.WANITA)
