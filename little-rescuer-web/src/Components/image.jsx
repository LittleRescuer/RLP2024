import Image from "next/image";
import { ArticleComponent } from "./articleComponent";

export function ImageComponent(props) {
  return (
    props.image && (
      <li className="border-t border-gray-100 border-opacity-30 p-5 flex flex-col md:flex-row gap-5 justify-center">
        <Image
          src={props.image.url}
          width={400}
          height={400}
          alt="Little Rescuer Client Image"
          className="rounded-xl border border-gray-100 border-opacity-15"
        />
        <ArticleComponent image={props.image} />
      </li>
    )
  );
}
