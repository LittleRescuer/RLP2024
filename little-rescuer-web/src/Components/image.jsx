import Image from "next/image";

export function ImageComponent(props) {
  return (
    props.image && (
      <li className="border-t border-gray-100 border-opacity-30 p-5 flex gap-5 justify-center">
        <img
          src={decodeURI(props.image)}
          width={400}
          height={400}
          alt="Little Rescuer Client Image"
          className="rounded-xl"
        />
      </li>
    )
  );
}
