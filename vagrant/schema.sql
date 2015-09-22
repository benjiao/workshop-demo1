CREATE SCHEMA IF NOT EXISTS `blogdb`;
USE `blogdb`;

-- -----------------------------------------------------
-- Table `blogdb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogdb`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `username` VARCHAR(255) NULL COMMENT '',
  `name` VARCHAR(255) NULL COMMENT '',
  `password` VARCHAR(100) NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogdb`.`post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogdb`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `title` VARCHAR(255) NULL COMMENT '',
  `content` TEXT NULL COMMENT '',
  `user_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_post_user_idx` (`user_id` ASC)  COMMENT '',
  CONSTRAINT `fk_post_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogdb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO `blogdb`.`user` (`id`, `username`, `name`, `password`) VALUES (1, 'benjie', 'Benjie Jiao', 'password');

