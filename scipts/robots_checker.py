from urllib.robotparser import RobotFileParser

def check_robots_txt(url, user_agent):
    robot_parser = RobotFileParser()
    robot_parser.set_url(url + "/robots.txt")
    robot_parser.read()
    return robot_parser.can_fetch(user_agent, url)
