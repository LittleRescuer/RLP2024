export function ArticleComponent(props) {
  return (
    <article className="flex flex-col items-center justify-center gap-5 ml-0 md:ml-5">
      <button className="bg-white hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded">
        <a
          download={props.image.pathname}
          href={props.image.downloadUrl}
          className="inline-flex items-center"
        >
          <svg
            className="fill-current w-4 h-4 mr-2"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
          </svg>
          <span>Download</span>
        </a>
      </button>
      <p>
        <strong>Date: </strong>{" "}
        {new Date(
          Number(props.image.pathname.replace(".jpg", ""))
        ).toLocaleString()}
      </p>
    </article>
  );
}
