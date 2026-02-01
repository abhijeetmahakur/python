import numpy as np

def generate_data():
    data = np.random.randn(1000)
    return data

def analyze(data):
    mean = np.mean(data)
    std = np.std(data)

    result = {
        "1_std": np.sum((data >= mean-std) & (data <= mean+std)),
        "2_std": np.sum((data >= mean-2*std) & (data <= mean+2*std)),
        "3_std": np.sum((data >= mean-3*std) & (data <= mean+3*std))
    }
    return result

data = generate_data()
distribution = analyze(data)
print(distribution)
