# BharatDub AI — Language Support

## Current language mapping

The Gradio UI uses these language codes:

| Display name | Code |
|---|---|
| English | `en` |
| Spanish | `es` |
| French | `fr` |
| German | `de` |
| Italian | `it` |
| Turkish | `tr` |
| Russian | `ru` |
| Dutch | `nl` |
| Czech | `cs` |
| Arabic | `ar` |
| Chinese (Simplified) | `zh-cn` |
| Japanese | `ja` |
| Korean | `ko` |
| **Hindi** | **`hi`** |
| Hungarian | `hu` |

## Hindi

Hindi is already present in the original project's `language_mapping`:

```python
'Hindi': 'hi'
```

The dubbing pipeline passes the target language code to:

```python
tts.tts_to_file(..., language=self.target_language)
```

Therefore, when `Hindi` is selected, the target TTS language is `hi`.

This clone also makes **Hindi the default target language** in the Gradio interface.

## Important note

Hindi support depends on the installed XTTS model version actually exposing `hi`. Before a production deployment, run:

```bash
tts --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --list_language_idx
```

and confirm that `hi` appears in the installed model's language list.

For the current XTTS configuration, Coqui documents `hi` as one of the language codes in the model configuration.
