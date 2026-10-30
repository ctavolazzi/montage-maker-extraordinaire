# How to work in this repo

CT (Christopher) owns this. He taps play on the notebook in his Drive; it pulls videos from his
iCloud (via icloudpd, optional) plus any video in his Drive, and saves a montage to
My Drive/Montage Maker/Montages. His phone has no free storage, so nothing may go through the phone.

The live copy is in his Drive (file id `1RPOsx9zA6j41aV9m5n1plK1qzO9Bcvz3`). When
`montage.ipynb` changes here, update that file too.

- **Keep it simple.** One notebook, `montage.ipynb`, run on Google Colab. No settings. Add a
  feature only when CT asks.
- **Free.** No paid APIs. Any AI runs inside the Colab notebook.
- **Works from his phone, computer off.** Nothing may depend on his computer.
- **Never change the uploaded videos.** Write only to the `Montages` folder.
- **No em dashes.**
- Commits go to `main`, small, plain messages. Don't open or watch pull requests unless CT asks.
