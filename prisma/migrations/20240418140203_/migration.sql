-- CreateTable
CREATE TABLE "SourceBook" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,

    CONSTRAINT "SourceBook_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Book" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "decription" TEXT NOT NULL,
    "source_book_id" INTEGER NOT NULL,

    CONSTRAINT "Book_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Theme" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "book_id" INTEGER NOT NULL,

    CONSTRAINT "Theme_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Book" ADD CONSTRAINT "Book_source_book_id_fkey" FOREIGN KEY ("source_book_id") REFERENCES "SourceBook"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Theme" ADD CONSTRAINT "Theme_book_id_fkey" FOREIGN KEY ("book_id") REFERENCES "Book"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
