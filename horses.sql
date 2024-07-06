-- Table: Horses
CREATE TABLE Horses (
    HorseID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    OwnerID INT NOT NULL,
    Trainer VARCHAR(255),
    YearBorn INT CHECK (YearBorn >= 1900 AND YearBorn <= EXTRACT(YEAR FROM CURRENT_DATE)),
    Gender ENUM('Filly', 'Colt'),
    Gait ENUM('Trotting', 'Pacing'),
    SelectedStakes TEXT,
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);

-- Table: Owners
CREATE TABLE Owners (
    OwnerID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20),
    BillingAddress TEXT,
    CardNumber VARCHAR(16),
    CCV VARCHAR(4),
    ExpDate DATE,
    CardName VARCHAR(255)
);

-- Table: Trainer
CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(20),
    Address TEXT
);

-- Table: HorsesTrainers (Link Table)
CREATE TABLE HorsesTrainers (
    HorseID INT NOT NULL,
    TrainerID INT NOT NULL,
    FOREIGN KEY (HorseID) REFERENCES Horses(HorseID),
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID),
    PRIMARY KEY (HorseID, TrainerID)
);

-- Sample data insert for testing
INSERT INTO Owners (Name, Email, PhoneNumber, BillingAddress, CardNumber, CCV, ExpDate, CardName)
VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St, Anytown, USA', '1234123412341234', '123', '2024-12-31', 'John Doe');

INSERT INTO Horses (Name, OwnerID, Trainer, YearBorn, Gender, Gait, SelectedStakes)
VALUES
('Speedy', 1, 'Jane Smith', 2018, 'Colt', 'Trotting', 'Stake1, Stake2');
