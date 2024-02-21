# Modal EdgeTTS 🗣️

this is a simple python app that let's you deploy microsoft's [EdgeTTS](https://pypi.org/project/edge-tts) as an HTTP api via modal <:)


here's a [lorem ipsum demo](https://cdn-crayo.com/crayo-admin%2Florem-ipsum.mp3) using this repo



### Setup

1. If you haven't signed up for Modal, do so [here](https://modal.com)
2. Log in via CLI with `modal token new` ([docs](https://modal.com/docs/reference/cli/token))
3. Run `modal deploy main.py` to deploy the app

YAY! You've got a working API. Now let's test it out.

### Run via CURL

1. Open the terminal
2. Run `curl -X POST https://your_url.modal.run -d '{"text": "hello world"}' -H "Content-Type: application/json --output file.mp3`
   
### Run via Fetch
`const response = await fetch(
      "https://your_url.modal.run",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: text,
        }),
      },
    );
  const data = await response.arrayBuffer();
  const buffer = Buffer.from(data);
`

#### Additional notes
This code does not include authentication. If you expose the modal url to client, it *can* be abused. If you call inferencing from a server, it's not a big deal imo. I personally use a simple secret setup as a redundancy measure since we call inferencing in a rate-limited backend. Refer to the [authentication docs](https://modal.com/docs/guide/webhooks#authentication) for best practices.


built w/ ❤️ by [aleem](https://twitter.com/aleemrehmtulla)
