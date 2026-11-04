"""Standalone ComfyUI extension for FLUX.2 Klein text + image references."""

from comfy_api.latest import ComfyExtension

from .flux_klein_text_encode import FluxKleinTextEncode


class FluxKleinTextEncodeExtension(ComfyExtension):
    async def get_node_list(self):
        return [FluxKleinTextEncode]


def comfy_entrypoint():
    return FluxKleinTextEncodeExtension()


__all__ = ["comfy_entrypoint"]
