"use client";

import { ImageComponent } from "@/Components/image";
import Image from "next/image";
import { useEffect, useState } from "react";

export default function Home() {
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:3000/api/getImages")
      .then(response => response.json())
      .then(data => {
        setLoading(false);
        setImages(data.images?.map(image => image));
      })
      .catch(e => console.error("Error fetching images", e));
  }, []);

  return (
    <main className="text-center container ml-auto mr-auto w-3/5 mt-20 md:mt-40">
      <header className="flex items-center gap-5 flex-col md:flex-row">
        <Image
          src="/logo.jpg"
          width={200}
          height={200}
          alt="Little Rescuer Logo"
          className="rounded-full"
        />
        <div className="flex flex-col justify-between text-center md:text-left gap-5">
          <h1 className="text-6xl">Little Rescuer</h1>
          <p className="text-xl opacity-85">
            Your assistance robot in the roads
          </p>
        </div>
      </header>

      <section className="mt-32">
        <h2 className="text-4xl opacity-80"> Image Carrousel </h2>
        <ul className="mt-5">
          {loading ? (
            <div className="border-t border-gray-100 border-opacity-30 p-5 flex gap-5 justify-center relative">
              <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
            </div>
          ) : images.length > 0 ? (
            images?.map((image, index) => (
              <ImageComponent key={index} image={image} />
            ))
          ) : (
            "No images available"
          )}
        </ul>
      </section>
    </main>
  );
}
