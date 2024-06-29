import { NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const uploadDir = path.join(process.cwd(), "/public");

if (!fs.existsSync(uploadDir)) {
  fs.mkdir(uploadDir);
}

export async function POST(request) {
  try {
    const { image } = await request.json();
    if (!image) {
      return NextResponse.json({ error: "No image provided" }, { status: 400 });
    }

    // Decode image from base64
    const base64data = image.replace(/^data:image\/\w+;base64,/, "");
    const buffer = Buffer.from(base64data, "base64");

    // Generate unique file name
    const fileName = `${Date.now()}.png`;
    const filePath = path.join(uploadDir, fileName);

    // Save image in the server
    fs.writeFileSync(filePath, buffer);

    return NextResponse.json({
      message: "Image uploaded succesfully",
      fileName,
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
