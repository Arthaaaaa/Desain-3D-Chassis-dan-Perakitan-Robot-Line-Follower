# Desain 3D Chassis dan Perakitan Robot Line Follower (Tinkercad to Webots)

Repositori proyek simulasi Robot Line Follower menggunakan model 3D dari Tinkercad dan simulasi fisika pada Webots (Mata Kuliah Praktikum IoT - Bab 7).

## Struktur Repositori

- `models/` — File model 3D hasil ekspor Tinkercad (`tinker.obj`, `obj.mtl`).
- `worlds/` — Lingkungan simulasi Webots (`line_follower_world_v2.wbt`), tekstur lintasan (`textures/track.png`), dan model terpisah untuk rotasi roda (`models/chassis.obj`, `wheel_1.obj`, `wheel_2.obj`).
- `controllers/line_follower_ctrl/` — Source code pengontrol robot berbasis Python dengan algoritma PD Control (`line_follower_ctrl.py`).

## Cara Menjalankan

1. Buka aplikasi **Webots**.
2. Pilih **File** > **Open World...** dan buka `worlds/line_follower_world_v2.wbt`.
3. Tekan tombol **Play** (`▶`) untuk menjalankan simulasi robot mengikuti lintasan garis hitam.
