def generate_reply(user_message: str) -> str:
        is_after_hours = is_off_hours()
        system_content = BUSINESS_INSTRUCTIONS
      
        if is_after_hours:
            system_content += "\nIt is currently outside business hours."

        completion = client.chat.completions.create(
                                                        model="gpt-4.1-mini",
                                                        messages=[
                                                                    {"role": "system", "content": system_content},
                                                                    {"role": "user", "content": user_message}
                                                                ],
                                                        max_tokens=120,
                                                        temperature=0.4,
                                                        )
        return completion.choices[0].message.content.strip()