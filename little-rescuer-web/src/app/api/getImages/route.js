import { NextResponse } from "next/server";
const fs = require("fs");
const path = require("path");

const readBase64 = imagePath => {
  const image = fs.readFileSync(imagePath);
  return "data:image/jpeg;base64," + image.toString("base64");
};

export async function GET() {
  try {
    const imagesDir = path.join(process.cwd(), "/public");

    const getImages = async () => {
      const files = fs.readdirSync(imagesDir);
      const imagesBase64 = files.map(fileName => {
        if (fileName === "favicon.ico") return;
        return readBase64(path.join(imagesDir, fileName));
      });
      return imagesBase64;
    };

    const images = await getImages();
    let imagesArray = [];
    for (const img of images) {
      if (img) {
        imagesArray.push(img);
      }
    }

    return NextResponse.json({ images: imagesArray });
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
