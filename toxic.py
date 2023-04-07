import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt




def toxic_AI(text):
    max_features = 10000
    max_len = 200
    embedding_size = 128
    filters = 250
    kernel_size = 3
    hidden_dims = 128
    input_layer = Input(shape=(max_len,), dtype='int32')
    embedding_layer = Embedding(input_dim=max_features, output_dim=embedding_size, input_length=max_len)(input_layer)
    conv_layer = Conv1D(filters=filters, kernel_size=kernel_size, activation='relu')(embedding_layer)
    pooling_layer = GlobalMaxPooling1D()(conv_layer)
    hidden_layer = Dense(hidden_dims, activation='relu')(pooling_layer)
    output_layer = Dense(1, activation='sigmoid')(hidden_layer)
    model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    df = pd.read_csv('toxic.csv')

    comment = df['comment'].values
    toxic = df['toxic'].values

    x_train, x_test, y_train, y_test = train_test_split(comment, toxic, test_size=0.2, random_state=42)

    # Векторизация текстовых данных
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(x_train)
    x_train = tokenizer.texts_to_sequences(x_train)
    x_test = tokenizer.texts_to_sequences(x_test)

    x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_len)
    x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=max_len)

    loaded_model = tf.keras.models.load_model('model_5.h5')
    # Преобразовать текст в числовой формат
    text_seq = tokenizer.texts_to_sequences(text)
    # Заполнить до максимальной длины последовательности
    text_seq_padded = tf.keras.preprocessing.sequence.pad_sequences(text_seq, maxlen=max_len)
    # Получить предсказание
    prediction = loaded_model.predict(text_seq_padded)
    return prediction
