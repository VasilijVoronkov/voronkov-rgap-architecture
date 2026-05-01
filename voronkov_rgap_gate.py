import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_rgap_gate_funnel():
    """
    Visualizes the R.G.A.P. Gate as a Phasic Classification funnel.
    Reference: Voronkov (2026). R.G.A.P. Architecture.
    """
    # Создаем геометрию затвора (конус/воронка)
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, 5, 30)
    U, V = np.meshgrid(u, v)
    
    X = V * np.cos(U)
    Y = V * np.sin(U)
    Z = V # Воронка направлена вверх

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Рисуем саму воронку затвора (сетка)
    ax.plot_wireframe(X, Y, Z, color='cyan', alpha=0.1)

    # Генерируем "Мусор" (галлюцинации ИИ) над воронкой
    trash_x = np.random.normal(0, 3, 500)
    trash_y = np.random.normal(0, 3, 500)
    trash_z = np.random.uniform(5, 8, 500)
    ax.scatter(trash_x, trash_y, trash_z, color='purple', s=2, alpha=0.3, label='Entropic Hallucinations')

    # Генерируем "Чистый сигнал", прошедший сквозь затвор
    sig_t = np.linspace(0, 6, 200)
    sig_x = 0.1 * np.sin(sig_t * 5)
    sig_y = 0.1 * np.cos(sig_t * 5)
    sig_z = sig_t
    ax.plot(sig_x, sig_y, sig_z, color='magenta', linewidth=3, label='Deterministic Output')

    ax.set_title('ZONE 3: R.G.A.P. GATE: PHASIC CLASSIFICATION')
    ax.set_zlim(0, 8)
    ax.view_init(elev=15, azim=30)
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_rgap_gate_funnel()
