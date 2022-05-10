CREATE TABLE Presidency_Data.tbl_steres (
  steres_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  steres_name VARCHAR(120)  NULL,
  steres_description VARCHAR(120)  NULL,
  steres_address VARCHAR(120)  NULL,
  steres_active BIT  NULL,
  steres_preducts_sc_id INT  NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_preducts(preducts_id),
  steres_is_valid BIT NOT NULL DEFAULT 1,
  steres_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  steres_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  steres_deleted_at DATETIME NULL,
  steres_creator_id INT NULL,
  steres_updater_id INT NULL,
  steres_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_user (
  user_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  user_name VARCHAR(120)  NULL,
  user_nick VARCHAR(120)  NULL,
  user_is_valid BIT NOT NULL DEFAULT 1,
  user_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  user_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  user_deleted_at DATETIME NULL,
  user_creator_id INT NULL,
  user_updater_id INT NULL,
  user_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_preducts (
  preducts_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  preducts_name VARCHAR(120)  NULL,
  preducts_description VARCHAR(120)  NULL,
  preducts_active BIT  NULL,
  preducts_is_valid BIT NOT NULL DEFAULT 1,
  preducts_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  preducts_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  preducts_deleted_at DATETIME NULL,
  preducts_creator_id INT NULL,
  preducts_updater_id INT NULL,
  preducts_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_sheppingcart (
  sheppingcart_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  sheppingcart_ree_mame VARCHAR(120)  NULL,
  sheppingcart_user_sc_id INT  NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_user(user_id),
  sheppingcart_preducts_sc_id INT  NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_preducts(preducts_id),
  sheppingcart_is_valid BIT NOT NULL DEFAULT 1,
  sheppingcart_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  sheppingcart_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  sheppingcart_deleted_at DATETIME NULL,
  sheppingcart_creator_id INT NULL,
  sheppingcart_updater_id INT NULL,
  sheppingcart_deleter_id INT NULL
)
;

GO
