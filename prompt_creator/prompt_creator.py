class PromptCreator:
    def create_prompt(self, system_prompt, context, user_display_name, user_message, custom_instructions, ai_name):
        prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
        prompt += f"{system_prompt}<|eot_id|>\n"

        for turn in context:
            username = turn['user'].replace("T@ai_name@T", ai_name)
            prompt += f"<|start_header_id|>{username}<|end_header_id|>{turn['message']}<|eot_id|>\n"

        prompt += f"<|start_header_id|>{user_display_name}<|end_header_id|>{user_message}<|eot_id|>\n"

        if custom_instructions:
            custom_instructions = custom_instructions.replace(
                "{ai_name}", ai_name)
            prompt += f"<|begin_of_text|>{custom_instructions}<|eot_id|>\n"

        prompt += f"<|start_header_id|>{ai_name}<|end_header_id|>"
        return prompt
