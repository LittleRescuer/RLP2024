import { NextResponse } from "next/server";
import { put } from "@vercel/blob";

export async function POST(request) {
  try {
    const fileName = `${Date.now()}.jpg`;

    const formData = await request.formData();
    const file = formData.get("image");

    const blob = await put(fileName, file, { access: "public" });
    if (!blob) throw new Error("Could not upload blob");
    console.log(blob);

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
