import { NextResponse } from "next/server";
import { list } from "@vercel/blob";

const fs = require("fs");
const path = require("path");

const readBase64 = imagePath => {
  const image = fs.readFileSync(imagePath);
  return "data:image/jpeg;base64," + image.toString("base64");
};

export async function GET() {
  try {
    const images = await list();

    return NextResponse.json({ images: images.blobs });
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}
