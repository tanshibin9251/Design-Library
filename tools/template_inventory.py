"""Create a complete source-based improvement queue, without editing templates."""
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'build'))
import dlib
from template_review import inspect_template

PHOTO_FIRST = {'restaurant', 'culinary', 'photography', 'interior', 'furniture',
               'travel', 'events', 'realestate', 'beauty', 'fashion', 'pets',
               'agriculture', 'massage', 'health'}
DIGITAL = {'saas', 'tech', 'coding', 'gaming', 'finance', 'legal', 'government',
           'logistics', 'language', 'exam', 'psychology'}
IDEAS = {
 'restaurant': '首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应',
 'culinary': '菜谱成品、食材与分步图片；不把随机菜品当同一道菜',
 'photography': '成套作品、项目封面与画廊；保留一致色调、裁切和作品顺序',
 'interior': '空间大图、项目案例、材质细节和改造前后；页脚分组对齐',
 'furniture': '家具主图、材质/尺寸细节、场景图；补选项/价格/缺货演示',
 'travel': '目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界',
 'events': '活动/婚礼视觉、场地与项目封面；时间、票务与预约状态清楚',
 'realestate': '房源封面、室内/户型视觉；筛选、零结果、收藏和询盘演示',
 'beauty': '空间/服务/产品摄影；真实案例须有来源，不冒充库存图为成果',
 'fashion': '系列与商品图、材质细节；尺码/颜色/购物车演示保持一致',
 'construction': '项目/工序/团队示意摄影；询价表单、项目详情和页脚完善',
 'medical': '诊所/服务场景示意图；预约、验证与请求反馈，不宣称已预约',
 'health': '服务场景和空间摄影；预约/计划选择与手机菜单完善',
 'massage': '空间、服务与技法示意摄影；预约选择和演示反馈',
 'fitness': '训练空间与课程特色图；课程选择/价格/预约状态完善',
 'education': '教学环境/课程封面；课程详情、课表与试课请求演示',
 'pets': '动物/空间/商品摄影；服务或商品选项与请求反馈',
 'agriculture': '农场、时令食材和产品图；购物与订阅演示',
 'automotive': '车型/车间与服务过程；比较/规格/报价和查询演示',
 'homeservices': '服务/项目过程示意图；报价、服务区域与请求反馈',
 'saas': '优先产品界面和功能图；修正 CTA、价格/试用演示，不用风景替代产品',
 'tech': '产品界面、技术图解或服务成果视觉；核对功能说明与 CTA',
 'coding': '保留 IDE/代码界面；课程/练习演示、键盘和手机菜单完善',
 'gaming': '保留游戏/插画风格；补活动/设备视觉、手机交互和性能检查',
 'finance': '优先数据图表和信息排版；补计算边界与咨询演示，摄影可选',
 'legal': '保留文档式排版；可选空间图，完善服务详情、咨询和页脚',
 'government': '任务/目录与可读性优先；可选社区摄影，补查询和无结果状态',
 'logistics': '保留流程/轨迹图；可选运营摄影，明确查询和估算的演示数据',
 'language': '保留课程/学习界面；可选学习场景，补分级测试与选课反馈',
 'exam': '保留仪表/学习计划；补测验、解释与空状态，不必强加背景照片',
 'psychology': '保留平静排版与图解；可选自然背景，检查动效降级及阅读体验',
 'music': '作品/演出或教学场景视觉；播放/课程/购物演示与触屏反馈',
 'coworking': '空间、设施与活动摄影；工位/方案选择与看场地请求',
 'faith': '社区/活动摄影；日程、信息层级、手机导航和页脚',
 'nonprofit': '项目与活动示意图；明确数据和捐赠按钮的演示边界',
 'corporate': '团队/服务/案例示意视觉；服务详情、询盘与整齐页脚',
 'agency': '案例主视觉与交付细节；服务/案例/询价流程及页脚',
 'media': '文章/内容封面与栏目层级；搜索、空结果、阅读及页脚',
 'arts': '作品和课程封面；保留画廊构图，补详情与交互反馈',
}


def inspect():
    rows = []
    common_css = dlib.runtime_css()
    for slug in dlib.template_slugs():
        item = dlib.load_template(slug, full=False)
        directory = item['dir']
        signals = inspect_template(directory)
        footer = (directory / 'footer.html').read_text(encoding='utf-8') if (directory / 'footer.html').exists() else ''
        nav = (directory / 'nav.html').read_text(encoding='utf-8') if (directory / 'nav.html').exists() else ''
        classes = re.search(r'<footer[^>]*class="([^"]+)"', footer)
        own_footer = classes.group(1).split() if classes else []
        footer_check = bool('class="cols"' in footer and 'foot' not in own_footer and not any(re.search(r'\.' + re.escape(c) + r'[^{}]*\.cols\s*\{[^}]*display\s*:\s*grid', nav + common_css) for c in own_footer))
        industries = item['ind']
        if slug == 'cafe-bakery':
            group, priority = '已完成示范', 0
        elif set(industries) & PHOTO_FIRST:
            group, priority = '优先摄影与布局升级', 1
        elif set(industries) & DIGITAL:
            group, priority = '保留插画/排版，完善功能', 3
        else:
            group, priority = '按行业补视觉与演示流程', 2
        notes = []
        for industry in industries:
            if industry in IDEAS and IDEAS[industry] not in notes:
                notes.append(IDEAS[industry])
        if not notes:
            notes.append('按本模板用途补主视觉/特色图、导航和核心演示反馈，不统一换成摄影风格')
        if footer_check:
            notes.append('页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug）')
        if slug == 'modern-saas':
            notes.insert(0, '已确认：试用/视频 CTA 目的不一致，Features 重名')
        if slug == 'restaurant-warm':
            notes.insert(0, '已确认：结账总额与明细不符，存在重复页面名')
        if slug == 'cafe-bakery':
            notes = ['已批准的高清外链摄影 + 手机导航/表单演示 + 三栏页脚；不重复安排升级']
        rows.append(dict(slug=slug, name=item['name'], zh=item['zh'], group=group,
                         priority=priority, pages=len(item['pagelist']), industries=industries,
                         signals=signals, footer_needs_review=footer_check,
                         recommendation='；'.join(notes)))
    return rows


def write():
    rows = inspect()
    counts = Counter(row['group'] for row in rows)
    lines = ['# 全部 Website 模板优化候选清单', '',
             '状态：本清单已获执行授权；实际改动与验证范围见 [执行记录](TEMPLATE_UPGRADE_STATUS.md)。本脚本只检查源码，不执行升级。', '',
             f'本清单完整覆盖 {len(rows)} 套模板。按元数据、全部页面源码与既有抽查整理；不是对每套模板逐页进行过浏览器测试。', '',
             '## 如何判断', '',
             '- 图片数量只统计 HTML 的 img 引用；SVG、CSS 插画和背景图不等于缺图。不能用“0 张 img”直接判定设计不好。',
             '- 占位数量指 class=ph 的块；表单数量和 return false 仅是静态线索，不代表全部没有 JS，也不证明已接真实后台。',
             '- 摄影类补 Google 找到且核验来源的高清外链图片，按 Crumb & Co 的方式处理裁切、加载、署名和失效回退；不下载照片原文件。',
             '- 数字/图解类保留自己的视觉语言，优先产品截图、示意图和交互完善；不强行插入风景或人物照片。',
             '- 所有待升级模板都应检查主 CTA、移动导航、空/成功/错误状态、页脚布局和导出；这些是验收要求，不是已证实全部有 bug。', '',
             '## 建议分批', '']
    for group in ['已完成示范', '优先摄影与布局升级', '按行业补视觉与演示流程', '保留插画/排版，完善功能']:
        lines += [f'### {group}（{counts[group]} 套）', '',
                  '| 模板 / slug | 页数 | 图片 / 占位 / 表单 | 建议 |', '|---|---:|---|---|']
        for row in sorted((r for r in rows if r['group'] == group), key=lambda r: r['slug']):
            signal = row['signals']
            label = f"{row['name']} · {row['zh']}"
            url = f"https://designlibrary.grownotic.com/#/template/{row['slug']}"
            lines.append(f"| [{label}]({url})<br>`{row['slug']}` | {row['pages']} | {signal['images']} / {signal['placeholders']} / {signal['forms']} | {row['recommendation']} |")
        lines.append('')
    lines += ['## 执行规则', '',
              '建议先从已确认问题的 Modern SaaS、Restaurant Warm，以及摄影回报明显的家具/空间/餐饮模板选小批执行。每批先核对具体页面，再搜图和改版；不依据本清单自动批量替换。', '',
              '高清标准、图片使用和全站后续工作见 IMPLEMENTATION_PLAN.md。当前完整数据同时保存在 TEMPLATE_IMPROVEMENT_INVENTORY.json；可按 slug 选择要执行的条目。', '']
    (ROOT / 'docs/TEMPLATE_IMPROVEMENT_QUEUE.md').write_text('\n'.join(lines), encoding='utf-8')
    (ROOT / 'docs/TEMPLATE_IMPROVEMENT_INVENTORY.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(total=len(rows), groups=dict(counts)), ensure_ascii=False))


if __name__ == '__main__':
    write()
