/*
  Warnings:

  - Added the required column `updated_at` to the `Book` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `SourceBook` table without a default value. This is not possible if the table is not empty.
  - Added the required column `updated_at` to the `Theme` table without a default value. This is not possible if the table is not empty.

*/
-- CreateEnum
CREATE TYPE "ROLE" AS ENUM ('USER', 'ADMIN');

-- AlterTable
ALTER TABLE "Book" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL;

-- AlterTable
ALTER TABLE "SourceBook" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL;

-- AlterTable
ALTER TABLE "Theme" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL;

-- CreateTable
CREATE TABLE "User" (
    "id" SERIAL NOT NULL,
    "username" TEXT NOT NULL,
    "telegram_id" INTEGER NOT NULL,
    "role" "ROLE" NOT NULL DEFAULT 'USER',
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_username_key" ON "User"("username");

-- CreateIndex
CREATE UNIQUE INDEX "User_telegram_id_key" ON "User"("telegram_id");
