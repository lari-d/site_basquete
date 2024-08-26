-- Criação da tabela Usuario
CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(15) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    altura DECIMAL(5, 2) NULL,
    posicao VARCHAR(50) NULL,
    mao_dominante ENUM('Direita', 'Esquerda') NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tipo_usuario ENUM('usuario', 'administrador') DEFAULT 'usuario',
    UNIQUE (email)
);

--Criação da tabela Admin
CREATE TABLE Administrador (
    id_administrador INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Criação da tabela Time
CREATE TABLE Time (
    id_time INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
    -- Outros detalhes do time podem ser adicionados aqui
);

-- Criação da tabela Local
CREATE TABLE Local (
    id_quadra INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    localizacao VARCHAR(255)
    -- Outros detalhes do local podem ser adicionados aqui
);

-- Criação da tabela Partida
CREATE TABLE Partida (
    id_jogo INT AUTO_INCREMENT PRIMARY KEY,
    data DATETIME NOT NULL,
    id_time_casa INT NOT NULL,
    id_time_visitante INT NOT NULL,
    id_quadra INT NOT NULL,
    FOREIGN KEY (id_time_casa) REFERENCES Time(id_time),
    FOREIGN KEY (id_time_visitante) REFERENCES Time(id_time),
    FOREIGN KEY (id_quadra) REFERENCES Local(id_quadra)
);

-- Criação da tabela Reserva
CREATE TABLE Reserva (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_quadra INT NOT NULL,
    data DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_quadra) REFERENCES Local(id_quadra)
);

-- Criação da tabela Pontuacao
CREATE TABLE Pontuacao (
    id_pontuacao INT AUTO_INCREMENT PRIMARY KEY,
    id_jogo INT NOT NULL,
    id_jogador INT NOT NULL,
    pontos INT NOT NULL,
    FOREIGN KEY (id_jogo) REFERENCES Partida(id_jogo),
    FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador)
);

-- Criação da tabela Jogador
CREATE TABLE Jogador (
    id_jogador INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_time INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_time) REFERENCES Time(id_time)
);

-- Criação da tabela Jogador_Time (tabela de junção para o relacionamento muitos-para-muitos)
CREATE TABLE Jogador_Time (
    id_jogador INT NOT NULL,
    id_time INT NOT NULL,
    PRIMARY KEY (id_jogador, id_time),
    FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador),
    FOREIGN KEY (id_time) REFERENCES Time(id_time)
);
