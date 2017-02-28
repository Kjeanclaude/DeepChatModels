import tensorflow as tf
import chatbot
from utils import Config

# ==============================================================================================================================
# Parser for command-line arguments.
# - Each flag below is formatted in three columns: [name] [default value] [description]
# - Each flag's value can later be accessed via: FLAGS.name
# - The flags are shown in alphabetical order (by name).
# ==============================================================================================================================

TEMP="/home/brandon/terabyte/Datasets/ubuntu_dialogue_corpus"

flags = tf.app.flags
flags.DEFINE_integer("batch_size", 64, "Batch size to use during training.")
flags.DEFINE_string("data_dir", TEMP, "Directory containing the data files.")
flags.DEFINE_string("data_name", "ubuntu", "For now, either 'ubuntu' or 'wmt'.")
flags.DEFINE_boolean("decode", False, "If true, will activate chat session with user.")
flags.DEFINE_integer("vocab_size", 40000, "English vocabulary size.")
flags.DEFINE_integer("layer_size", 512, "Size of each model layer.")
flags.DEFINE_float("learning_rate", 0.5, "Learning rate.")
flags.DEFINE_float("lr_decay", 0.98, "Decay factor applied to learning rate.")
flags.DEFINE_float("max_gradient", 5.0, "Clip gradients to this value.")
flags.DEFINE_integer("max_train_samples", 0, "Limit training data size (0: no limit).")
flags.DEFINE_integer("num_layers", 3, "Number of layers in the model.")
flags.DEFINE_integer("steps_per_ckpt", 100, "How many training steps to do per checkpoint.")
flags.DEFINE_string("ckpt_dir", "out", "Directory in which checkpoint files will be saved.")
flags.DEFINE_string("num_buckets", 2, "number of pad buckets to use")
FLAGS = flags.FLAGS

if __name__ == "__main__":

    import os
    print("data dir is ", FLAGS.data_dir)
    os.listdir(FLAGS.data_dir)
    config = Config(FLAGS)
    buckets = [(5, 10), (20, 30), (40, 50)]
    if len(buckets) > int(FLAGS.num_buckets): buckets = buckets[:int(FLAGS.num_buckets)]
    chatbot = chatbot.Chatbot(config, buckets)

    if FLAGS.decode:
        chatbot.decode()
    else:
        chatbot.train()
