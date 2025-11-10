import tensorflow as tf
from tensorflow import keras

print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Version: {keras.__version__}")
print("---")
print("Available GPUs:")

# This will list your Mac's GPU if tensorflow-metal is working
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    print(f"Found {len(gpu_devices)} GPU(s):")
    for gpu in gpu_devices:
        print(f"- {gpu.name}")
else:
    print("No GPU found. TensorFlow will use the CPU.")