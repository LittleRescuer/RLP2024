"use client";

import { ImageComponent } from "@/components/image";
import Image from "next/image";
import { useEffect, useState } from "react";

export default function Home() {
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`https://little-rescuer.vercel.app/api/getImages/${Date.now()}`, {
      method: "GET",
      headers: {
        "Cache-Control": "no-cache",
      },
    })
      .then(response => response.json())
      .then(data => {
        setLoading(false);
        setImages(data.images?.map(image => image));
      })
      .catch(e => console.error("Error fetching images", e));
  }, []);

  return (
    <>
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
          {loading ? (
            <div className="border-t border-gray-100 border-opacity-30 p-5 flex gap-5 justify-center relative">
              <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
            </div>
          ) : (
            <ul className="mt-5 flex flex-col-reverse">
              {images.length > 0 ? (
                images?.map((image, index) => (
                  <ImageComponent key={index} image={image} />
                ))
              ) : (
                <li>No images available</li>
              )}
            </ul>
          )}
        </section>
      </main>
      <footer className="w-full border-t border-gray-100 border-opacity-30 px-10 md:px-[20%] py-5 md:py-10 mr-auto text-center md:text-left text-white text-opacity-75">
        &copy; 2024 Little Rescuer - Universitat Autònoma de Barcelona
      </footer>
    </>
  );
}
