with open('fix_projects_index.py', 'r') as f:
    fix_content = f.read()

# Extract proj_idx = ... + get_footer(1)
start_idx = fix_content.find("proj_idx = get_tailwind_head")
end_idx = fix_content.find("with open('./projects/index.html', 'w')")

if start_idx != -1 and end_idx != -1:
    new_proj_idx = fix_content[start_idx:end_idx].strip()
    
    with open('tailwind_redesign.py', 'r') as f:
        tw_content = f.read()
        
    tw_start = tw_content.find("proj_idx = get_tailwind_head")
    tw_end = tw_content.find("with open('./projects/index.html', 'w')")
    
    if tw_start != -1 and tw_end != -1:
        updated_tw_content = tw_content[:tw_start] + new_proj_idx + "\n" + tw_content[tw_end:]
        with open('tailwind_redesign.py', 'w') as f:
            f.write(updated_tw_content)
        print("Successfully updated tailwind_redesign.py")
